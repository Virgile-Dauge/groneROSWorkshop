
(cl:in-package :asdf)

(defsystem "my_pkg-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "myService" :depends-on ("_package_myService"))
    (:file "_package_myService" :depends-on ("_package"))
  ))