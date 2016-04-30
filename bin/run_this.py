from helloworld import hello
print dir(hello)
import sys
print sys.path

print "Hello World!.... Deploying"
hello = hello.Hello()
hello.app.run(host="0.0.0.0")
