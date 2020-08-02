# AudioBookReaderUsingPython

Requirements :

          Python
          
          import pyttsx3   // pip install pyttsx3
          
          import PyPDF2
          
pyttsx3 is a text to speech conversion library in python.It can works in offline and compatible with both
python 2 and 3.

Usage :
      
          Changing Voice, Rate, Volume 
      
I prefer to use a trick to do this. See my code for that.



PyPDF2 is a Pure-Python library built as a PDF toolkit. It is capable of:

    extracting document information (title, author, …)
    
    splitting documents page by page
    
    merging documents page by page
    
    cropping pages
    
    merging multiple pages into a single page
    
    encrypting and decrypting PDF files
    and more!

By being Pure-Python, it should run on any Python platform without any dependencies on external libraries. It can also work entirely on StringIO objects rather than file streams, allowing for PDF manipulation in memory. It is therefore a useful tool for websites that manage or manipulate PDFs.

<b>I use a loop to do it like which page to which page I want to listen.</b>
