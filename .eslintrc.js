"use strict";

// Stolen and modified from https://github.com/walmartlabs/eslint-config-defaults
module.exports = {
  "env": {"browser": true, "jquery": true},
  "globals": {"_": true},
  "rules": {
    // Enforces getter/setter pairs in objects
    "accessor-pairs": 0,
    // treat var statements as if they were block scoped
    "block-scoped-var": 0,
    // specify the maximum cyclomatic complexity allowed in a program
    "complexity": 0,
    // require return statements to either always or never specify values
    "consistent-return": 0,
    // specify curly brace conventions for all control statements
    "curly": [2, "all"],
    // require default case in switch statements
    "default-case": 2,
    // enforces consistent newlines before or after dots
    "dot-location": [2, "object"],
    // encourages use of dot notation whenever possible
    "dot-notation": 0,
    // require the use of === and !==
    "eqeqeq": 1,
    // make sure for-in loops have an if statement
    "guard-for-in": 2,
    // disallow the use of alert, confirm, and prompt
    "no-alert": 0,
    // disallow use of arguments.caller or arguments.callee
    "no-caller": 0,
    // disallow lexical declarations in case clauses
    "no-case-declarations": 0,
    // disallow division operators explicitly at beginning of regular expression
    "no-div-regex": 0,
    // disallow else after a return in an if
    "no-else-return": 0,
    // disallow use of empty destructuring patterns
    "no-empty-pattern": 0,
    // disallow comparisons to null without a type-checking operator
    "no-eq-null": 0,
    // disallow use of eval()
    "no-eval": 2,
    // disallow adding to native types
    "no-extend-native": 2,
    // disallow unnecessary function binding
    "no-extra-bind": 0,
    // disallow fallthrough of case statements
    "no-fallthrough": 0,
    // disallow the use of leading or trailing decimal points in numeric literals
    "no-floating-decimal": 0,
    // disallow the type conversions with shorter notations
    "no-implicit-coercion": 0,
    // disallow use of eval()-like methods
    "no-implied-eval": 0,
    // disallow this keywords outside of classes or class-like objects
    "no-invalid-this": 2,
    // disallow usage of __iterator__ property
    "no-iterator": 0,
    // disallow use of labeled statements
    "no-labels": 0,
    // disallow unnecessary nested blocks
    "no-lone-blocks": 0,
    // disallow creation of functions within loops
    "no-loop-func": 2,
    // disallow the use of magic numbers
    "no-magic-numbers": 0,
    // disallow use of multiple spaces
    "no-multi-spaces": 0,
    // disallow use of multiline strings
    "no-multi-str": 2,
    // disallow reassignments of native objects
    "no-native-reassign": 2,
    // disallow use of new operator for Function object
    "no-new-func": 0,
    // disallows creating new instances of String,Number, and Boolean
    "no-new-wrappers": 0,
    // disallow use of new operator when not part of the assignment or comparison
    "no-new": 0,
    // disallow use of octal escape sequences in string literals, such as
    // var foo = "Copyright \251";
    "no-octal-escape": 0,
    // disallow use of (old style) octal literals
    "no-octal": 0,
    // disallow reassignment of function parameters
    "no-param-reassign": 0,
    // disallow use of process.env
    "no-process-env": 0,
    // disallow usage of __proto__ property
    "no-proto": 0,
    // disallow declaring the same variable more then once
    "no-redeclare": 0,
    // disallow use of assignment in return statement
    "no-return-assign": 0,
    // disallow use of `javascript:` urls.
    "no-script-url": 0,
    // disallow comparisons where both sides are exactly the same
    "no-self-compare": 0,
    // disallow use of comma operator
    "no-sequences": 0,
    // restrict what can be thrown as an exception
    "no-throw-literal": 0,
    // disallow usage of expressions in statement position
    "no-unused-expressions": 0,
    // disallow unnecessary .call() and .apply()
    "no-useless-call": 0,
    // disallow unnecessary concatenation of literals or template literals
    "no-useless-concat": 0,
    // disallow use of void operator
    "no-void": 0,
    // disallow usage of configurable warning terms in comments: e.g. todo
    "no-warning-comments": 0,
    // disallow use of the with statement
    "no-with": 2,
    // require use of the second argument for parseInt()
    "radix": 0,
    // requires to declare all vars on top of their containing scope
    "vars-on-top": 0,
    // require immediate function invocation to be wrapped in parentheses
    "wrap-iife": 0,
    // require or disallow Yoda conditions
    "yoda": 0,
    // disallow trailing commas in object literals
    "comma-dangle": 0,
    // disallow assignment in conditional expressions
    "no-cond-assign": 0,
    // disallow use of console
    "no-console": 0,
    // disallow use of constant expressions in conditions
    "no-constant-condition": 0,
    // disallow control characters in regular expressions
    "no-control-regex": 0,
    // disallow use of debugger
    "no-debugger": 0,
    // disallow duplicate arguments in functions
    "no-dupe-args": 2,
    // disallow duplicate keys when creating object literals
    "no-dupe-keys": 2,
    // disallow a duplicate case label.
    "no-duplicate-case": 0,
    // disallow the use of empty character classes in regular expressions
    "no-empty-character-class": 0,
    // disallow empty statements
    "no-empty": 2,
    // disallow assigning to the exception in a catch block
    "no-ex-assign": 0,
    // disallow double-negation boolean casts in a boolean context
    "no-extra-boolean-cast": 0,
    // disallow unnecessary parentheses
    "no-extra-parens": 2,
    // disallow unnecessary semicolons
    "no-extra-semi": 2,
    // disallow overwriting functions written as function declarations
    "no-func-assign": 2,
    // disallow function or variable declarations in nested blocks
    "no-inner-declarations": [2, "functions"],
    // disallow invalid regular expression strings in the RegExp constructor
    "no-invalid-regexp": 0,
    // disallow irregular whitespace outside of strings and comments
    "no-irregular-whitespace": 0,
    // disallow negation of the left operand of an in expression
    "no-negated-in-lhs": 0,
    // disallow the use of object properties of the global object (Math and JSON) as functions
    "no-obj-calls": 0,
    // disallow multiple spaces in a regular expression literal
    "no-regex-spaces": 0,
    // disallow sparse arrays
    "no-sparse-arrays": 0,
    // Avoid code that looks like two expressions but is actually one
    "no-unexpected-multiline": 0,
    // disallow unreachable statements after a return, throw, continue, or break statement
    "no-unreachable": 1,
    // disallow comparisons with the value NaN
    "use-isnan": 0,
    // ensure JSDoc comments are valid
    "valid-jsdoc": 2,
    // ensure that the results of typeof are compared against a valid string
    "valid-typeof": 0,
    // require that all functions are run in strict mode
    "strict": [2, "global"],
    // enforce spacing inside array brackets
    "array-bracket-spacing": 0,
    // disallow or enforce spaces inside of single line blocks
    "block-spacing": 0,
    // enforce one true brace style
    "brace-style": [2, "1tbs", { "allowSingleLine": true }],
    // require camel case names
    "camelcase": 2,
    // enforce spacing before and after comma
    "comma-spacing": 0,
    // enforce one true comma style
    "comma-style": 0,
    // require or disallow padding inside computed properties
    "computed-property-spacing": 0,
    // enforces consistent naming when capturing the current execution context
    "consistent-this": 0,
    // enforce newline at the end of file, with no multiple empty lines
    "eol-last": 0,
    // require function expressions to have a name
    "func-names": 0,
    // enforces use of function declarations or expressions
    "func-style": 0,
    // this option enforces minimum and maximum identifier lengths (variable names, property names etc.)
    "id-length": 0,
    // require identifiers to match the provided regular expression
    "id-match": 0,
    // this option sets a specific tab width for your code
    "indent": [2, 2],
    // specify whether double or single quotes should be used in JSX attributes
    "jsx-quotes": 0,
    // enforces spacing between keys and values in object literal properties
    "key-spacing": [2, { "beforeColon": false, "afterColon": true }],
    // disallow mixed "LF" and "CRLF" as linebreaks
    "linebreak-style": 0,
    // enforces empty lines around comments
    "lines-around-comment": 0,
    // specify the maximum depth that blocks can be nested
    "max-depth": 0,
    // specify the maximum length of a line in your program
    "max-len": [2, 80, 4, {ignoreComments: true, ignoreUrls: true, ignorePattern: "^\\s*var\\s.+=\\s*require\\s*\\("}],
    // specify the maximum depth callbacks can be nested
    "max-nested-callbacks": 0,
    // limits the number of parameters that can be used in the function declaration.
    "max-params": 0,
    // specify the maximum number of statement allowed in a function
    "max-statements": 0,
    // require a capital letter for constructors
    "new-cap": 2,
    // disallow the omission of parentheses when invoking a constructor with no arguments
    "new-parens": 0,
    // allow/disallow an empty newline after var statement
    "newline-after-var": 0,
    // disallow use of the Array constructor
    "no-array-constructor": 2,
    // disallow use of bitwise operators
    "no-bitwise": 0,
    // disallow use of the continue statement
    "no-continue": 0,
    // disallow comments inline after code
    "no-inline-comments": 0,
    // disallow if as the only statement in an else block
    "no-lonely-if": 0,
    // disallow mixed spaces and tabs for indentation
    "no-mixed-spaces-and-tabs": 2,
    // disallow multiple empty lines
    "no-multiple-empty-lines": 0,
    // disallow negated conditions
    "no-negated-condition": 0,
    // disallow nested ternary expressions
    "no-nested-ternary": 0,
    // disallow use of the Object constructor
    "no-new-object": 2,
    // disallow use of unary operators, ++ and --
    "no-plusplus": 0,
    // disallow use of certain syntax in code
    "no-restricted-syntax": 0,
    // disallow space between function identifier and application
    "no-spaced-func": 2,
    // disallow the use of ternary operators
    "no-ternary": 0,
    // disallow trailing whitespace at the end of lines
    "no-trailing-spaces": 2,
    // disallow dangling underscores in identifiers
    "no-underscore-dangle": 0,
    // disallow the use of Boolean literals in conditional expressions
    "no-unneeded-ternary": 0,
    // require or disallow padding inside curly braces
    "object-curly-spacing": [2, "never"],
    // allow just one var statement per function
    "one-var": 0,
    // require assignment operator shorthand where possible or prohibit it entirely
    "operator-assignment": 0,
    // enforce operators to be placed before or after line breaks
    "operator-linebreak": [2, "after"],
    // enforce padding within blocks
    "padded-blocks": 0,
    // require quotes around object literal property names
    "quote-props": 0,
    // specify whether double or single quotes should be used
    "quotes": [2, "single"],
    // Require JSDoc comment
    "require-jsdoc": 0,
    // enforce spacing before and after semicolons
    "semi-spacing": 0,
    // require or disallow use of semicolons instead of ASI
    "semi": 2,
    // sort variables within the same declaration block
    "sort-vars": 0,
    // require a space before/after certain keywords
    "keyword-spacing": 0,
    // require or disallow space before blocks
    "space-before-blocks": [2, "always"],
    // require or disallow space before function opening parenthesis
    "space-before-function-paren": [2, "never"],
    // require or disallow spaces inside parentheses
    "space-in-parens": [2, "never"],
    // require spaces around operators
    "space-infix-ops": 2,
    // Require or disallow spaces before/after unary operators
    "space-unary-ops": 0,
    // require or disallow a space immediately following the // or /* in a comment
    "spaced-comment": 0,
    // require regex literals to be wrapped in parentheses
    "wrap-regex": 0,
    // enforce or disallow variable initializations at definition
    "init-declarations": 0,
    // disallow the catch clause parameter name being the same as a variable in the outer scope
    "no-catch-shadow": 0,
    // disallow deletion of variables
    "no-delete-var": 2,
    // disallow labels that share a name with a variable
    "no-label-var": 0,
    // disallow shadowing of names such as arguments
    "no-shadow-restricted-names": 2,
    // disallow declaration of variables already declared in the outer scope
    "no-shadow": 0,
    // disallow use of undefined when initializing variables
    "no-undef-init": 0,
    // disallow use of undeclared variables unless mentioned in a /*global */ block
    "no-undef": 2,
    // disallow use of undefined variable
    "no-undefined": 0,
    // disallow declaration of variables that are not used in the code
    "no-unused-vars": 2,
    // disallow use of variables before they are defined
    "no-use-before-define": 1
  }
};
