(import os) (import sys)
(import validators)
(import [jeefies [Content]])

(defclass User []
	(defn __init__ [self path name]
		"initialize the function"
		(setv self.con (Content path name))
	)
	(defn get [self name-or-email]
		(if (= (len (get (setx con (self.con.get name-or-email)) 1)) 1)
			(return (self.con.get #*(get con 1)))
			con
		)
	)
	(defn has [self name-or-email]
		(if (self.con.has name-or-email)
			(return True)
			(return False)
		)
	)
	(defn allname [self]
		(return (lfor x (self.con.allname) :if not (validators.email x)))
	)
	(defn all [self]
		(return (self.con.all))
	)
	(defn allitem [self]
		(return (self.con.allitem))
	)
	(defn rm [self name-or-email]
		(return (self.con.rm name-or-email))
	)
	(defn reset [self]
		(return (self.con.reset))
	)
)
