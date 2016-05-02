from helloworld import hello
import sys

args = sys.argv
hello = hello.Hello()
hello.app.run(host="0.0.0.0", port=args[1])
