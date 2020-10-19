(import os sys)
;;(import logging logging.config)
(import validators)
(import [jeefies [Content]])
(import [.supports [gravatar]])
;;(import [jeefies.flask_self [get_user]])

(defclass User []
	"A hy function for content of the user"
	(defn __init__ [self path]
		"initialize the function"
		(setv self.con (Content path "user"))
		;;(print (self.con.allitem))
	)
	(defn get-orig [self name-or-email]
		"get the info by the email or the name"
		(setv con (self.con.get name-or-email))
		(if-not con (return None))
		(setv length (len (get con 1)))
		(if (= length 1)
			(return (self.con.get (get con 1 0)))
			(return con)
		)
	)
	(defn get [self email-or-mane]
		"return the user checked type"
		(return (user :from-for (self.get-orig email-or-name)))
	)
	(defn has [self name-or-email]
		"check if the content has the user by name or the email"
		(if (self.con.has name-or-email)
			(return True)
			(return False)
		)
	)
	(defn allname [self]
		"return all user's name but email"
		(return (self.check-mail (self.con.allname)))
	)
	(defn allval [self]
		"return all value includes emails"
		(return (self.con.all))
	)
	(defn allitem [self]
		"return all item format by (username, value), except the email"
		(return (self.check-mail (self.con.allitem)))
	)
	(setv all allname)
	(defn add [self index list-of-values]
		"add content by index and a list or tuple of values"
		(self.con.add index list-of-values)
	)
	(defn add-user [self user]
		"add a user by user class"
		(self.con.add #*user.con)
	)
	(defn rm [self name-or-email]
		"remove the name or the email with the name
		 if remove name, the email would keep"
		(return (self.con.rm name-or-email))
	)
	(defn reset [self]
		"reset the content(clear the data)"
		(return (self.con.reset))
	)
	#@(staticmethod (defn check-mail [mail]
		"check and return the matched item in the mail list or tuple"
		(return (lfor x mail :if (not (validators.email x)) x))
	))
	(defn __str__ [self]
		"return the string of the function()"
		(return (str self.con))
	)
	(defn __repr__[self]
		"return the workplace and the function info"
		(return (py "'<User at {}>'.format(self.con.pl)"))
	)
	(defn __set__ [self obj val]
		"This function doesn't support set attribute "
		(raise (TypeError "This function doesn't support set attribute"))
	)
	;;(setv __setattr__ __set__)
	(defn __iter__ [self]
		"iteration preparing"
		(setv self._st 0)
		(return self)
	)
	(defn __next__ [self]
		"The `next` would use it"
		(setv con (self.con.get (get (self.all) self._st)))
		(return (user :from-con con))
	)
)

;;(logging.config.fileConfig "logging.cnf")
;;(setv logger (.getLogger logging "logfile"))

(defclass user []
	(defn __init__ [self &optional [name ""] [passwd ""] [permission ""] [email ""] [full-name ""] [description ""] [country-place ""] &kwonly [from-con []] [out False]]
		;;(logger.debug "user init")
		(if from-con
		(do 
		(setv from-con (list from-con))
		(if* (!= (len (get from-con 1)) 6)
			(while (< (len (get from-con 1)) 6)
			((. from-con [1] append) "")
			)
		)
		(setv [self.name [self.passwd self.per self.email self.full-name self.des self.pl]] from-con)
		)
		(do
		(setv self.name name)
		(setv self.passwd passwd)
		(setv self.per permission)
		(setv self.email email)
		(setv self.full-name full-name)
		(setv self.des description)
		(setv self.pl country-place)
		))
		(setv self.gravatar (gravatar self.email 256))
	)
	(defn isself [self]
		(= self.name (get_user))
	)
	(defn isauthor [self]
		(= self.per 16)
	)
	#@(property
	(defn linedes [self]
		(lfor x ((. self des split) "\n") :if x x)
	))
	#@(property
	(defn con [self]
		(return [self.name [self.passwd self.per self.email self.full-name self.des self.pl]])
	))
	(defn __setattr__ [self key val]
		;;(print "__setattr__ called")
		;;(logger.info (.format "updating {} to {}" key val))
		(self.__dict__.update #**{key val})
		val
	)
	;;(setv __setattr__ __set__)
	(defn __str__ [self]
		(return (.join "," (get self.con 1)))
	)
)


(defn get_user [error]
	(import [flask [request]])
	(setv name (request.cookies.get (+ "name" request.remote_addr)))
	(if name (return name) (return (error)))
)
