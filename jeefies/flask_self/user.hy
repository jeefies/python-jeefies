(import os) (import sys)
(import validators)
(import [jeefies [Content]])

(defclass User []
	"A hy function for content of the user"
	(defn __init__ [self path]
		"initialize the function"
		(setv self.con (Content path "user"))
	)
	(defn get [self name-or-email]
		"get the info by the email or the name"
		(if (= (len (get (setx con (self.con.get name-or-email)) 1)) 1)
			(return (self.con.get (get con 1 0)))
			(return con)
		)
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
	(defn __iter__ [self]
		"iteration preparing"
		(setv self._st 0)
		(return self)
	)
	(defn __next__ [self]
		"The `next` would use it"
		(setv key (get (self.all) self._st))
		(return (, key (self.con.get key)))
	)
)
