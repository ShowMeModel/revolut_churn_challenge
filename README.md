# Revolut churn challenge

A sample churn prevention solution for an FinTech app

## Challenge

1. Define a target metric to measure user engagement. How would you define an _engaged_ vs. _unengaged_ user?
    * Please provide the business justification and associated visualisations / rationale in choosing your definition of engagement

2. Using your logic from above, build a model (heuristic/statistical/ML) to classify _engaged_ and _unengaged_ users
    * Note that features which are directly correlated with your target metric could lead to overfitting

3. Let’s assume an _unengaged_ user is a churned user. Now suppose we use your model to identify unengaged users and implement some business actions try to convert them to engaged users (commonly known as reducing churn)
    * How would you set up a test/experiment to check whether we are actually reducing churn?
    * What metrics and techniques would you use to assess the impact of the business action?

## Data description

1. **devices.csv** - a table of devices associated with a user
    * **brand**: string corresponding to the phone brand
    * **user_id**: string uniquely identifying the user

2. **users.csv** - a table of user data
    * **user_id**: string uniquely identifying the user
    * **birth_year**: integer corresponding to the user’s birth year
    * **country**: two letter string corresponding to the user’s country of residence
    * **city**: two string corresponding to the user’s city of residence
    * **created_date**: datetime corresponding to the user’s created date
    * **ser_settings_crypto_unlocked**: integer indicating if the user has unlocked the crypto currencies in the app
    * **plan**: string indicating on which plan the user is on
    * **attributes_notifications_marketing_push**: float indicating if the user has accepted to receive marketing push notifications
    * **attributes_notifications_marketing_email**: float indicating if the user has accepted to receive
marketing email notifications
    * **num_contacts**: integer corresponding to the number of contacts the user has on Revolut
    * **num_referrals**: integer corresponding to the number of users referred by the selected user
    * **num_successful_referrals**: integer corresponding to the number of users successfully referred by the selected user (successfully means users who have actually installed the app and are able to use the product)

3. **notifications.csv** - a table of notifications that a user has received
    * **reason**: string indicating the purpose of the notification
    * **channel**: string indicating how the user has been notified
    * **status**: string indicating the status of the notification
    * **user_id**: string uniquely identifying the user
    * **created_date**: datetime indicating when the notification has been sent

4. **transactions.csv** - a table with transactions that a user made
    * **transaction_id**: string uniquely identifying the transaction
    * **transactions_type**: string indicating the type of the transaction
    * **transactions_currency**: string indicating the currency of the transaction
    * **amount_usd**: float corresponding to the transaction amount in USD
    * **transactions_state**: string indicating the state of a transaction
    * **COMPLETED** - the transaction was completed and the user's balance was changed
    * **DECLINED/FAILED** - the transaction was declined for some reason, usually pertains to
insufficient balance
    * **REVERTED** - the associated transaction was completed first but was then rolled back
later in time potentially due to customer reaching out to Revolut
    * **ea_cardholderpresence**: string indicating if the card holder was present when the transaction
happened
    * **ea_merchant_mcc**: float corresponding to the Merchant Category Code (MCC)
    * **ea_merchant_city**: string corresponding to the merchant’s city
    * **ea_merchant_country**: string corresponding to the merchant’s country
    * **direction**: string indicating the direction of the transaction
    * **user_id**: string uniquely identifying the user
    * **created_date**: datetime corresponding to the transaction’s created date

## Solution

### Description

### Overview

See a [slideshare presentation](https://www.slideshare.net/secret/f3PsT6ZJTEzTAT) for some additional comments and findings. 

### Requirements

Tested on Python `3.7+` and Macbook Pro (OS version `10.15.4`)

### Files
