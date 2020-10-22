;; use csv file to read and analyze some datas, based on csv file
;; delimeters = chr(1136), quotesep = chr(1138)
;; f one line context (with  no '\n')
;; depends on hy, also can use in pyhon.
;; author: jeef		,email: jeefy163@163.com
;; git: jeefies		,pypi: jeefy
;; python local version see content_py.py
;; use `content` to cache the class or just use Content for no cache
;; CACHE dict for cahce content

(import os csv codecs) ; import needs
(import [collections [namedtuple]])
(setv CACHE {}) ; set th cache dict for the content

(defclass ContextError [Exception] "error for the context error " (pys "pass")) ; class for the context error
(defclass PathError [Exception]  "error if the path is not avaliable"(pys "pass"))	 ; class for the path error

(defclass wait [] ; the class to manage context for using the function
	(defn --init-- [self] "init the using arg" (setv self.using False))
	#@(property (defn used [self] "get true if it's used" (return (bool self.using)))) ;get True if it's free
	#@(property (defn free [self] "get true if it's free" (return (not (bool self.using))))) ;get True if it's using
	(defn use [self] ;get the using permission
		"get the chance to run the code"
		(while True (if self.free (break))) ; wait for the function to have the using permission
		(setx self.using 1) ; set the function using
	)
	(defn release [self]
		"release the chance"
		;; if it's using, release the using
		(if self.used (setv self.using 0) (raise (ContextError "The class is free, can't release")))
	)
)

(defclass Content [wait]
	(defn --init-- [self work-place work-name &optional [use-dict False] [keys []]]
		"use-dict, keys for no use"
		(.--init-- wait self) ; init the waiting class
		(if (and (os.path.exists work-place) (os.path.isdir work-place)) ;check if the path is avaliable
		(do	(setv 	self.wkd (os.path.abspath work-place) ; absolute work path
				self.file (os.path.join self.wkd work-name) ; managed file name
				self.use-dict use-dict ; if use dict
				self.keys (tuple keys) ; the keys of the dict
				self.content {} ; the content
			)
			(.read self) ; read the content
		)
		(raise (PathError "work-place doesn't exists"))
	))
	(defn read [self] 
		"read the content from the file"
		(try
			(setv csvf (.open codecs self.file :encoding "utf-8"))
			;; if file is not exist, create a new one
			(except [Exception] (do (.open codecs self.file "x" :encoding "utf-8") (return False)))
		)
		(setv reader (self.get-reader csvf)) ; get the reader
		(.use self) ; start using the context chance
		(for [rline reader]
			;;(setv (. self content [(get rline 0)]) (get rline 1))
			(pys "self.content[rline[0]] = rline[1]")
		)
		(self.release) ; release the chance
	)
	(defn get-reader [self csvf]
		"return a generator to make it use less disk"
		;; get the reader according to the csvf
		(setv reader (.reader csv csvf :delimiter (chr 1136) :quotechar (chr 1138))) ; sep by chr(1136)
		(when self.use-dict (setv name (namedtuple "name" self.keys)))
		(for [line reader]
			(if self.use-dict
			(do
				(setv index (get line 0))
				(yield (, index (._asdict (name #*(cut line 1)))))
			)
			(yield (, (get line 0) (cut line 1)))
			)
		)
	)
	(defn writer [self csvf lines &optional header]
		"write the lines into the file, use writerows to write"
		(setv writer (.writer csv csvf self.keys :delimiter (chr 1136) :quotechar (chr 1138)))
		;; get the writer and write the headers according to the header arg
		(if* header (.writerow writer self.keys))
		(.use self)
		(.writerows writer lines)
		(.release self)
	)
	(defn update [self]
		"write in and read again"
		(setv lis [])
		(for [[k,v] (itmes self.content)]
			(if self.use-dict
				(.append lis (, k #*(.values v)))
				(.append lis (, k #*v))
			)
		)
		(.writer self (.open codecs self.file "w" :encoding "utf-8") lis)
		(.read self)
	)
	(defn add [self index vallist]
		"add the content by index and a value list"
		(.writer self (.open codecs self.file "a" :encoding "utf-8") [(, index #*vallist)])
		(pys "self.content[index] = tuple(vallist)")
	)
	(defn allname [self]
		"return all index name"
		(return (self.content.keys))
	)
	(setv all allname)
	(defn allval [self]
		"return all value list"
		(return (self.content.values))
	)
	(defn allitem [self]
		"return both index and value"
		(return (self.content.items))
	)
	(defn rm [self index]
		"remove the index and value and return"
		(.pop self.content index)
	)
	(setv remove rm)
	(defn find [self index]
		"find the index and return the value"
		(.get self.content index None)
	)
	(defn has [self index]
		"check whether the index is exist"
		(return (py "index in self.content"))
	)
	;;(defn findby [self col val]
	;;	(if-not self.use-dict (raise (TypeError "Please use use-dict mod to use this function")))
	;;)
	(defn --getitem-- [self key &optional extra-key]
		"enter the index and return the value"
		(print extra-key :end "")
		(return (get self.content key))
	)
	(defn --setitem-- [self key val]
		"set the index's value into val"
		(setv val (tuple val))
		(pys "self.content[key] = val")
		(return val)
	)
	(defn --delitem-- [self obj &optional objtype]
		(.pop self.content obj)
	)
	;;(defn --setattr-- [self key val &optional ty]
	;;	(raise (TypeError "'Content' object does not support assigment"))
	;;)
	(defn --str-- [self]
		"return the info of the class"
		(return (.format "<Content at {} by {}>" self.wkd self.keys))
	)
	(defn --repr-- [self]
		"the computer reading string"
		(return (.format "<Content at {}>" self.wkd))
	)
)
