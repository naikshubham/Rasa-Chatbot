## greet
* greet
  - utter_greet

## thank
* thank
  - utter_noworries

## goodbye
* bye
  - utter_bye

## bot1
* bot
  - utter_bot

<!-- ## validate1
* greet
  - utter_greet
* request_help
  - form_personaldetails
  - form{"name":"form_personaldetails"}
  - form{"name":null} -->

## status check1
* greet
  - utter_greet
* request_help
  - form_statuscheck
  - form{"name":"form_statuscheck}
  - form{"name":null}
* new
  - form_personaldetails
  - form{"name":"form_personaldetails"}
  - form{"name":null}

<!-- ## personaldetails1
* personal_details
  - utter_askname
  - form_personaldetails
  - form{"name":"form_personaldetails"}
  - form{"name":null}
  - action_deactivate_form
  - action_restart -->
