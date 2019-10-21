## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy
 
## processor query
* recommend_processor
	- processor_form
	- form{"name": "processor_form"}
	- form{"name": null}
	- utter_slots_values
* thankyou
   - utter_noworries

## product_nnp
* when_announced
  - utter_hot_chips
* what_announced
  - utter_hot_chips_announcement
> check_product

## product_nnp_i
> check_product
* ask_product_details{"nnpi":"nnp i"}
  - utter_nnp_i_details
* more_product_details
  - utter_more_nnp_i_details

## product_nnp_t
> check_product
* ask_product_details{"nnpt":"nnp t"}
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
