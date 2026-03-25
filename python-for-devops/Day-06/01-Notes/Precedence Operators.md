# Precedence of Operations in Python

## Introduction

Precedence of operations in Python defines the order in which different types of operators are evaluated in an expression. Operators with higher precedence are evaluated first.

## Examples

### Arithmetic Precedence

```python
result = 5 + 3 * 2
# Multiplication has higher precedence, so result is 11, not 16
```

# Operator Precedence (High → Low)

1. Parentheses
   ( )
2. Unary Operators
   ++   --   !   ~   + (unary)   - (unary)
3. Multiplication / Division / Modulus
   *   /   %
4. Addition / Subtraction
   +   -
5. Relational Operators
   <   >   <=   >=
6. Equality Operators
   ==   !=
7. Logical AND
   &&
8. Logical OR
   ||
9. Assignment Operators
   =   +=   -=   *=   /=   %=

## Notes
- Parentheses `( )` always execute first.
- Same precedence → Associativity rule applies.
- Use parentheses to make expressions clear and avoid bugs.