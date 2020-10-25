(import os codecs)

(import click)

(import [.rdconf [reader]]
	[.sdml [easy-mail-sender :as ems mdToHtml readFile]
	)

#@((.command click)
#@((.option click "-c" "--config" :help "The config file to read" :default "sdml.conf")
#@((.option click "-r" "--receivers" :help "The email address who need to receive the email" :prompt "receivers for the email: ")
#@((.option click "-s" "--subject" :help "The title of the email" :prompt "Subject for the email: ")
#@((.option click "-tf" "--txt-file" :help "The content file of the email with 'txt' filetype.
defual is body.txt" :default "body.txt")
#@((.option click "-hf" "--html-file" :help "The html type content of the email with 'html', 'htm' filetype.\nNo css style sheets in it and no arguments in.\nDefualt is 'index.html'" :default "index.html")
#@((.option click "-mf" "--markdown-file" :help "The markdown file of the email with 'md' 'mkd' 'markdown' ... filetype.")
#@((.option click "-af" "--add-files" :help "The files send with the email, files sep with ','")
(defn main [config receivers subject txt-file html-file markdown-file add-files]
	(setv 	conf (reader config)
		plain-text (readFile txt-file)
		html (readFile html-file)
		mkd (mdToHtml markdown-file)
		files (.split add-files ",")
	)
	(when (= files add-files) (setv files [files]))
	(setv html (+ html "\n\n" mkd))
)
