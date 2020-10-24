;; Hy Lisp to send-mail
(import logging logging.config)
(import os sys codecs smtplib [. [mime]])
(import [email.utils [parseaddr formatdate formataddr]]
	[email.header [Header]]
	)

(setv logger logging)

(defn sanitize-address [addr &optional [encoding "utf-8"]]
	"sanitize one email address for sending email"
	(if* (isinstance addr str)
		(setv addr (parseaddr addr))
	)
	(setv [nm addr] addr)
	(setv nm (.encode (Header nm encoding)))
	;;(setv addr (.encode addr "ascii"))
	(return (formataddr (, nm addr)))
)
(defn sanitize-addresses [addresses &optional [encoding "utf-8"]]
	"sanitize some email address for sending email, return a generation"
	(defn ana [e] (sanitize-address e encoding))
	(return (gfor e addresses (ana e)))
)

(defn connect [smtp-host send-mail token-passwd &optional [port 465]]
	(try
		(.info logger "connecting to smtp...")
		(setv smtp (.SMTP_SSL smtplib smtp-host port))
		(.info logger "succeed connect with ssl")
	(except [Exception] (setv smtp (.SMTP smtplib smtp-host port)) (.info logger "succeed connect but without ssl"))
	)
	(.info logger "connect to" smtp-host ", with port:" port)
	;;(.connect smtp smtp-host port)
	(.connect smtp "smtp.163.com" 465)
	(.ehlo smtp)
	(.login smtp send-mail token-passwd)
	(return smtp)
)

(defn easy-mail-sender [smtp-host passwd send-mail tos subject content &optional [files-path []]]
	(setv msg (.MIMEMultipart mime.multipart))
	(setv (get msg "From") send-mail)
	(setv 	(get msg "To") (.join ", " (list (set(sanitize-addresses tos))))
		(get msg "Subject") subject
		content (.text.MIMEText mime content "plain" "utf-8")
	)
	(.attach msg content)
	(.info logger "add files")
	(for [file files-path]
		(setv part (.application.MIMEApplication mime (.read (.open codecs file "rb"))))
		(.add_header part "Content-Disposition" "attachment" 
			:filename (os.path.basename (os.path.abspath file)))
		(.attach msg part)
		(.info logger "add" file "finish")
	)
	(.info logger "sending...")
	(setv smtp (connect smtp-host send-mail passwd))
	(.sendmail smtp send-mail tos (str msg))
	(.close smtp)
	(.info logger "sending finish, \ncheck your email box to have a look")
	;;(return smtp)
)
