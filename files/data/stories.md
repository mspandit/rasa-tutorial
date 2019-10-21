## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## product_nnp_i
* when_announced
  - utter_hot_chips
* what_announced
  - utter_hot_chips_announcement
* ask_nnp_i_product_details
  - utter_nnp_i_details
* more_product_details
  - utter_more_nnp_i_details

## product_nnp_t
* when_announced
  - utter_hot_chips
* what_announced
  - utter_hot_chips_announcement
* ask_nnp_t_product_details
  - utter_nnp_t_details
* more_product_details
  - utter_more_nnp_t_details

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
