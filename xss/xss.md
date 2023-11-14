# Cross-Site Scripting (XSS)

## Types
### Stored
The web retreive data from its DB (or similar) and prints it into the web page. An attacker could use its username to add a payload such as `alert(1)` to exploit it.
### Reflected
The web takes attacker input and reflects it in the page. Then, an attacker could inject js commands.
### DOM
DOM-based XSS vulnerabilites arise when js takes data from an attacker-controllable source and sink that to dynamic code execution. The most common source for DOM XSS is the URL, which is typically accessed with the *windows.location* object.
The DOM (Document Object Model) is a web browser's hierachical representations of the elements on the page.

## Approach
Search for values that are present in the UI that can be modified by the user.
Then try to play around with their encoding, etc.
Input random strings and search them in the web-page (some of them maybe inside a potential vulnerable field)

### Usual vulnerable input fields
 - Usernames
 - Comments
 - Links
 - User email
 - Filenames

## TIPS
 - If `innerHTML` is used, script tags won't be executed (use img)
 - If working with *AngularJS* try to use SSTI to escale to an XSS (`{{constructor.constructor('alert(1)')()}}`)
