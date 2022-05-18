*** Settings ***
Library   DemoRobotLibrary

*** Test Cases ***
My Successful Test Case
    
    # Get the salutation string with the class defaults
    # Returns an English salutation string
    ${SALUTATION}=  Get My Salutation   Peter
    Log To Console  ${SALUTATION}

    # Get the Salutation and use named parameters
    ${SALUTATION}=  Get My Salutation   name=John
    Log To Console  ${SALUTATION}

    # Get the Salutation, use named parameters and override the language defaults
    ${SALUTATION}=  Get My Salutation   name=Franz  language=de
    Log To Console  ${SALUTATION}

    # Set the language and then get the salutation
    Set My Language   language=de
    ${SALUTATION}=  Get My Salutation   name=Thorsten
    Log To Console  ${SALUTATION}

    # Get the language
    ${LANGUAGE}=  Get My Language
    Log To Console  My language is ${LANGUAGE}

My Failed Test Case
    # Set an invalid language which will fail this test
    Set My Language   language=fr
