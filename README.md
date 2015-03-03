PayPerks Coding Exercise
========================

Requirements
------------

The PayPerks product team has been hard at work coming up with new ideas. The latest one is a new bonus feature for all users - a URL shortner - and now they're handing it over to the engineering team to build it.

Here's how the shortner should work:

1. A user inputs a URL into a text field.

2. The system generates a shortened URL which, when visited, redirects to the original URL. So, for example if the user entered 'http://www.example.com/this/is/a/long/url?foo=bar' then a shortened URL could be 'http://payperks.com/Fogmq'.

3. Visiting 'http://payperks.com/Fogmq' redirects to 'http://www.example.com/this/is/a/long/url?foo=bar'.

4. There should be an admin page that allows an admin user to view all shortened URLs the system has generated.

5. Provide an API to allow creating new shortened urls and retrieving information from existing ones.

Bonus!
------

Provide an easy way to start the project to prove all criterias were met. It can be a script, vagrant image, etc. Use your creativity!

Instructions
------------

1. Using Django (or Flask / Rails / Sinatra), build a self-contained application that implements the above requirements. Feel free to use any additional third party libraries that you'd like.

2. This is a very basic (and not complete) implementation. You can use this as a starting point should you wish.

3. Make any assumptions that you need to. This is an opportunity to showcase your skills, so if you want to, implement the shortner with any additional features you'd like to see.

4. Please include any instructions for getting your app up and running locally in a README in the project root directory.

5. We are evaluating solutions based on the architecture and quality of the code. Show us just how beautiful, clean and pragmatic your code can be.

Now it's time to sit down with a cup of coffee, maybe put on some of your favorite music and most importantly, enjoy!
