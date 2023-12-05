"""
Area of triangle.
   area = (base * hight) / 2

Suppose base is 10 and height is 6
What is area?
Area is (10*6)/2, which is 30.
Let python calculate it.

>>> (10*6)/2
30.0

This expression works, but it is not
reusable. Try this instead:
>>> base=10
>>> height=6
>>> (base*height)/2
30.0

Now we can change the values of base
and height, and our expression still works..
>>> base=4
>>> height=20
>>> (base*height)/2

That is a lot of typing. Lets combine lines.
Then we can be lazier.

>>> base=4 ; height=20; (base*height)/2
>>> base=10; height=6; (base*height)/2

Should we make our code sorter by using
the names 'b' and 'h' instead of 'base'
and 'height' in our formula? Consider the
following formula:

    (1) area = (base*height)/2
    (2) a = (b*h)/2

These formula all do the same thing, but the
first is much more readable, and much easier
to understand, because it uses names that are
descriptive, and that are well known to people
who have studied geometry.

But we will shorten it for now:

>>> b=4; h=20; (b*h)/2
>>> b=10; h=6; (b*h)/2

This works, and we already know we are talking
about the area of triangles.

But look at this:

>>> def fn(): b=4 ; h=20 ; return (b*h)/2
>>> fn()

>>> def fn(): b=10 ; h=6 ; return (b*h)/2
>>> fn()

This seems hardly an improvement, but be
patient. We can move the assignment statemente
inside the parenthesis:

>>> def fn(b=4,h=20 ; return (b*h)/2

>>> b=10 ; h=6; (b*h)/2
# This is much shorter to type!
# Lets create a shortcut function. Lets
# call is 'fn' to remind us that it is
# a function.
def fn() : base=4; height=20; return ()

"""
