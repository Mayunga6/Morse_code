<!--- Overview --->
String to Morse code convertor
This python program receives input from the user, converts each letter of the input string 
into Morse code , and output the letters in collections each word separated by a line

<!--- Features --->
translator: receives the input string from the user as argument and has a dictionary 
where each letter in the string is compared if available in the key and the value 
of the dictionary assigned as the Morse code conversion.

<!--- Prerequisites --->
Python 3.x

<!--- Example --->
Enter the text to translate: Hello There 1234 678

<!--- Output --->
 * * * *
 *
 * - * *
 * - * *
 - - -

 -
 * * * *
 *
 * - *
 *

 * - - - -
 * * - - -
 * * * - -
 * * * * -

 - * * * *
 - - * * *
 - - - * *

<!--- Code Breakdown --->
Code Breakdown
translator function:
receives the input string from the user as argument. Since the 
morse code is the same for both uppercase and lowercase letters, each letter in the 
input string is first converted to lowercase. Each letter in the string is compared 
if available in the key and the value of the dictionary assigned as the Morse code 
conversion.

<!--- User Input section --->
User input section:
The user first receives a prompt where they enter the string/sentence the want to
convert to Morse code.

<!--- Notes --->
Notes
Ensure that the input is a sentence of strings or numbers.

<!--- License --->
License
This project is open-source and available under the MIT License.