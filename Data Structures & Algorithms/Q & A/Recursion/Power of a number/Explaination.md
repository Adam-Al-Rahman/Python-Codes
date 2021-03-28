In code we are recurring in class object. So, it is obvious that are code will contain the (self.) attribute.

# Q. How to calculate power of a number using recursion?

### <u>Answer</u>:

#### STEP-1: Recursive case - The flow

$x^{n} = x*x.....n time ...x$
$x^{a}*$  $x^{b}$ = $x^{a+b}$
$x^{n}$ = $x*x^{n-1}$

so, the first become:

```python
def power_s1(self,base,exp):  
  return base*self.power_s1(self,base,exp-1)
```

#### STEP-2: Base condition - The criterion

If we don't decide the base condition the function will recurs infinite time. Until it reach the max.

So, it is necessary that we put the base condition

Here, we can say that when base is equal to 1 and exponent is equal to one, the output will be one.

```python
if exp==0 or base==1:  
   return 1
```

#### STEP-3: Unintentional case - The constraint

There may be some input that will not work with this code. So, to indicate that we use assertion.

```python
assert exp>=0 and int(exp)==exp,'Exponent should be positive & integer'
```
