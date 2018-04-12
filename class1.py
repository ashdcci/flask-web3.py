
#from sys import exit
class MyClass(object):
	"This is my second class"
	a = 10
	def hellos(self):
		return 'hello world!!!'

	def show_the_login_form(self):
		return '''
            <form method="post">
                <p><input type=text name=username>
                <p><input type=submit value=Login>
            </form>
        '''
