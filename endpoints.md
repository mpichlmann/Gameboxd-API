# R5. Endpoint Documentation
## Auth Routes

## Route: /auth/register 
HTTP Request verb: POST

Arguments: None

Authentication: None, no authentication required as this route is intended for new users who are not yet in the system.

Required Data: Name, Email, Password

Description: This route allows new users to register an account which will create a new user in the database. 

Users must enter all of the required data fields otherwise they will encounter an error message specifying which fields are missing, example below: 

![MISSING FIELD PHOTO](https://i.imgur.com/XAAOlOr.jpg)

If all of the required fields are entered but not valid, such as the password being too short, or a user with that email already existing than another error message will be displayed, example below: 

![PASSWORD TOO SHORT](https://i.imgur.com/yV3UvOL.jpg)
![EMAIL ALREADY IN USE](https://i.imgur.com/8T5ylBH.jpg) 

If all of the required fields are entered and valid, then the new user will be created and added to the system with the users details being returned back, excluding the password for security purposes, example below:  

![SUCCESSFUL REGISTRATION PHOTO](https://i.imgur.com/vGi6Ufr.jpg) 

## Route: /auth/login
HTTP Request verb: POST

Arguments: None

Authentication: Upon successful login an access token will be generated and attached to the user for future authentication purposes. 

Required Data: Email Address, Password

Description: This route allows user to login and generate an access token which will be required for other functionality such as creating new reviews and comments, as well as editing/updating their own existing reviews and comments. 

Users must provide an email address that exists within the system as well as the correct corresponding password otherwise an error message will be displayed, which for security purposes does not specify which of the supplied fields, the email or the password, was incorrect. example below: 

![LOGIN DOESNT EXIST IMAGE](https://i.imgur.com/RpDmL6f.jpg)

If users enter a valid existing email address and the correct corresponding password, they will be returned their user details (excluding their password) as well as an access token that can be used for authentication involved in other functionality of the API, example below:    

![LOGIN SUCCESSFUL](https://i.imgur.com/1IrMrtK.jpg) 

## Games Routes

## Route: /games 
HTTP Request verb: GET 

Arguments: None

Authentication: None, as users need not be logged in to simply view the list of games available for reviewing.

Required Data: None

Description: Returns a list of games currently in the database that are available for reviewing, example below: 

![GAMES LIST IMAGE](https://i.imgur.com/PisWDX8.jpg)

## Route: /games/\<int:game_id>
HTTP Request verb: GET

Arguments: Integer of the game_id that is to be retrieved, for example Luigi's Mansion 3 has a game_id of 3 so doing a GET request on '/games/3' will return the information for Luigi's Mansion 3.

Authentication: None, as no users need not be logged in to simple retrieve a single game's information.

Required Data: None

Description: Retrives the information of a single specified game, example below: 

![SINGLE GAME IMAGE](https://i.imgur.com/LQDuzPd.jpg) 

If a game_id is specified that does not belong to a game that exists, an error message will be displayed, example below: 

![GAME GET NOT FOUND](https://i.imgur.com/tsN1e0i.jpg)

## Route: /games
HTTP Request verb: POST

Arguments: None

Authentication: Users must be authenticated with their access token and must be an authorised user (an admin) in order to successfully make use of this endpoint as only admins are allowed to add a new game. 

Required Data: Title, Genre, Description, Platforms

Description: Creates a new game in the database that can now be reviewed by other users. There are many times when a game is released on different platforms under the same name where the game itself is vastly different. For example, Harry Potter and The Chamber of Secrets has over four different versions all released on different platforms that all have very different gameplay despite all having the same title. For this reason, game information such as titles need not be unique, as the game_id will be the unique identifier. 

All information about the game must be provided otherwise an error message will be displayed, example below:

![GAMES MISSING FIELD IMAGE](https://i.imgur.com/VcHilt3.jpg)

If a user who is not an admin tries to create a new game in the database an error message will be displayed, example below: 

![GAMES ADD NOT ADMIN IMAGE](https://i.imgur.com/UNQIpWU.jpg) 

If a user who is an admin provides all details of the game then the request will be successful and the freshly created game details will be returned, example below: 

![GAMES ADD SUCCESS IMAGE](https://i.imgur.com/yttGEon.jpg) 

## Route: /games/\<int:game_id>
HTTP Request verb: PUT, PATCH 

Arguments: Integer of the game_id to be updated.

Authentication: Users must be authenticated with their access token and must be an admin in order to update game details. 

Required Data: Title, Genre, Description, Platforms. However not all fields are *required*, as only some of the fields may need updating.

Description: Allows admins to update game details, in the case of games being released on new platforms, or undergoing title changes etc. 

If a non admin tries to update game details an error message will be displayed, example below: 

![GAMES UPDATE NOT ADMIN](https://i.imgur.com/yrAPVQ0.jpg)

If a game_id is specified that does not belong to a game that exists, an error message will be displayed, example below: 

![GAME PUT NOT FOUND](https://i.imgur.com/ntSwRjK.jpg) 

If an admin updates a game with only a few of the fields, the request will still be successful as partial=True allows not all fields to be supplied, as in practice not all fields may need updating, example below: 

![GAMES UPDATE SUCCESS IMAGE](https://i.imgur.com/wpz7rSg.jpg)

## Route: /games/\<int:game_id>
HTTP Request verb: DELETE

Arguments: Integer of the game_id to be deleted. 

Authentication: Users must be authenticated with their access token and must be an admin in order to delete a game.

Required Data: None

Description: Deletes a game from the database. In practice it is not likely that a game would ever need to be deleted, however it is still import functionality to have. 

If a non-admin tries to delete a game, an error message will be displayed, example below: 

![GAME DELETE NOT ADMIN IMAGE](https://i.imgur.com/rNKTTfa.jpg)

If a game_id that does not belong to a game is specified a corresponding error message will be displayed, example below: 

![GAME DELETE NOT FOUND IMAGE](https://i.imgur.com/nDQgdAR.jpg) 

When an admin deletes a game by specifying the game_id in the endpoint, and the game_id matches a game that actually exists, a confirmation message will be displayed, example below: 

![GAME DELETE SUCCESS IMAGE](https://i.imgur.com/HuvoCn8.jpg) 

## Users Routes

## Route: /users 
HTTP Request verb: GET

Arguments: None

Authentication: None

Required Data: None

Description: Returns a list of all users (excluding passwords for security), example below:

![USERS GET SUCCESS IMAGE](https://i.imgur.com/AruCX1h.jpg)

## Route: /users/\<int:user_id>
HTTP Request verb: GET

Arguments: Integer of the user_id to be retrieved.

Authentication: None

Required Data: None

Description: Returns a single user (excluding password for security). 

If no such user exists that matches the specified ID then an error message will be displayed, example below: 

![USER GET ID DOES NOT EXIST](https://i.imgur.com/9Fe7dqS.jpg) 

If a user with the specified ID does exist, it will be returned successfully, example below: 

![USER ID GET SUCCESS](https://i.imgur.com/1T9nJIJ.jpg)

## Route: /users/\<int:user_id>
HTTP Request verb: PUT, PATCH

Arguments: Integer of the user_id to be updated.

Authentication: User must be authenticated with their access token matching and must be authorised to edit the users details by either being the same user to be updated or by being an admin, as users can only edit their own details and admins can edit anyones details. 

Required Data: Name, Email, Password. However not all fields are *required*, as only some of the fields may need updating.

Description: Allows users to edit their details. Not all details may need updating/editing and as such partial=True is used to allow the request to be successful even if not all fields are supplied. 

If a user attempts to edit a users detail without being that same user in question or without having administrator privileges an error message will be displayed, example below:

![USER UPDATE NOT OWNER OR ADMIN IMAGE](https://i.imgur.com/c8B74Eb.jpg)

If a user or admin tries to update the details of a user who does not exist, a corresponding error message will be displayed, example below: 

![USER UPDATE NOT FOUND](https://i.imgur.com/nx698si.jpg) 

If a user is the same user in question that is being updated, or if they are an admin, the request will successfully return the freshly updated user details (excluding the password) example below:

![USER UPDATE SUCCESS](https://i.imgur.com/6dqqnju.jpg)

## Route: /users/make_admin/\<int:user_id>
HTTP Request verb: PUT, PATCH

Arguments: Integer of the user_id beloning to the user who is to be made an admin.

Authentication: Users must be authenticated with their access token and must be an authorised admin in order to make other users an admin. 

Required Data: None

Description: Allows admin users to make other users into admins. 

If a non admin user tries to make another user into an admin, an error message will be displayed, example below: 

![NOT ADMIN MAKE ADMIN](https://i.imgur.com/CVcSaY2.jpg) 

If the specified user_id does not match a user who exists, an error message will be displayed, example below: 

![MAKE ADMIN USER NOT FOUND](https://i.imgur.com/iFMt98m.jpg) 

If a user who is an admin makes another user an admin and the user in question does in fact exist then a confirmation message will be displayed, example below: 

![MAKE ADMIN SUCCESS](https://i.imgur.com/fid5xHO.jpg)

## Route: /users/\<int:user_id>
HTTP Request verb: DELETE

Arguments: Integer of the user_id of the user to be deleted

Authentication: Users must be authenticated with their access token and must be an authorised admin in order to delete users. 

Required Data: None

Description: Allows admins to delete users from the database. 

If a user who is not an admin attempts to delete a user, an error message will be displayed, example below: 

![USER DELETE NOT ADMIN](https://i.imgur.com/SHaDsyK.jpg) 

If the specified user_id does not match a user that exists in the database, an error message will be displayed, example below:

![USER DELETE NOT FOUND](https://i.imgur.com/aGy8ZHv.jpg) 

If the user making the request is indeed an admin, and the specified user_id matches a user that exists than a confirmation 

![USER DELETE SUCCESS](https://i.imgur.com/xUUY7dA.jpg)

## Reviews Routes 

## Route: /reviews
HTTP Request verb: GET

Arguments: None

Authentication: None

Required Data: None

Description: Returns a list of all reviews along with the author of the review as well as all comments for each review, example below: 

![GET ALL REVIEWS](https://i.imgur.com/NeASqf9.jpg) 

## Route: /reviews/\<int:review_id>
HTTP Request verb: GET

Arguments: Integer of the review_id belonging to the review to be retrieved

Authentication: None

Required Data: None

Description: Returns a single review with a review_id matching the specified review_id along with the author of the review and all comments for the review, example below: 

![GET REVIEW ID SUCCESS](https://i.imgur.com/GQId62R.jpg) 

If no such review exists matching the specified review_id, an error message will be displayed, example below: 

![GET REVIEW NOT FOUND](https://i.imgur.com/0Zg0Mgr.jpg) 

## Route: /reviews/game/\<int:game_id>
HTTP Request verb: GET

Arguments: Integer of the game_id belonging to the game that all reviews for are to be retrieved. 

Authentication: None

Required Data: None

Description: Returns a list of all the reviews for the specified game, example below:

![GET REVIEWS FOR GAME SUCCESS](https://i.imgur.com/0DPB26d.jpg)

If no such game exists that matches the specified game_id an error message will be displayed, example below: 

![GET REVIEWS FOR GAME NOT FOUND](https://i.imgur.com/F2eJCKv.jpg) 

If no reviews exists for the specified game, then an error message will be displayed, example below: 

![GET REVIEWS FOR GAME NO REVIEWS](https://i.imgur.com/1EaZByG.jpg) 

## Route: /reviews/user/\<int:user_id>
HTTP Request verb: GET 

Arguments: Integer of the user_id belonging to the user whose reviews are to be retrieved. 

Authentication: None

Required Data: None

Description: Returns a list of all the reviews across all games by the specified user, example below: 

![GET REVIEWS FOR USER SUCCESS](https://i.imgur.com/rO3Uz0i.jpg) 

If no reviews have been authored by the specified user an error message will be displayed, example below: 

![GET REVIEWS FOR USER NO REVIEWS](https://i.imgur.com/PaevCDI.jpg)

If the specified user_id does not match an existing user an error message will be displayed, example below: 

![GET REVIEWS FOR USER NOT FOUND](https://i.imgur.com/mATe9EZ.jpg)

## Route: /reviews
HTTP Request verb: POST

Arguments: None

Authentication: Users must be logged in and authenticated with their access token before posting a new review.  

Required Data: Title, Rating, Body, Game_ID

Description: Allows users to create a new review for a given game. The request body must contain all of the required fields and be the correct data types otherwise an error will be displayed detailing what fields are missing and what data types are invalid, example below: 

![POST REVIEW MISSING FIELD INVALID DATA](https://i.imgur.com/w6u2gKc.jpg)

If all of the required fields are supplied and all of the data is valid, then the freshly made review will be returned, example below: 

![POST REVIEW SUCCESS](https://i.imgur.com/keW7hZ6.jpg)

## Route: /reviews/\<int:review_id>
HTTP Request verb: PUT, PATCH

Arguments: Integer of the review_id belonging to the review to be updated.

Authentication: Users must be authenticated with their access token and must be either the owner of the review or an admin to make changes to a review. 

Required Data: Title, Body, Rating. However not all fields are *required*, as only some of the fields may need updating.

Description: Allows users to make changes to a review. With partial=True users only need to supply the fields that they wish to update as users may not need to update all of the fields. If a user attempts to make changes to a review that is not theirs, an error will be displayed, example below: 

![PUT REVIEW NOT ADMIN](https://i.imgur.com/7Dybsht.jpg) 

If no such review exists that matches the specified review_id then an error will be displayed, example below: 

![PUT REVIEW NOT FOUND](https://i.imgur.com/B0jOJMy.jpg) 

If a user is an admin or the owner of the review, and they have correctly supplied the fields they wish to change the freshly updated review will be returned back, example below: 

![PUT REVIEW SUCCESS](https://i.imgur.com/3K77YUr.jpg) 

## Route: /reviews/\<int:review_id>
HTTP Request verb: DELETE

Arguments: Integer of the review_id belonging to the review to be deleted

Authentication: Users must be authenticated with their access token and must be either the owner of the review or an admin to delete the review. 

Required Data: None

Description: Allows review owners or admins to delete a review. If no such review matches the review_id specified an error message will be displayed, example below: 

![DELETE REVIEW NOT FOUND](https://i.imgur.com/0blICDu.jpg) 

If a user does not have the authorization to delete the review, an error message will be displayed, example below: 

![DELETE REVIEW NOT ADMIN](https://i.imgur.com/rTGdxnB.jpg)

If a user is either the owner of the review or an admin, and the specified review_id matches an existing review, a confirmation message will be displayed, example below: 

![DELETE REVIEW SUCCESS](https://i.imgur.com/3RHvYCW.jpg)

## Comments Routes 

## Route: /comments
HTTP Request verb: GET

Arguments: None

Authentication: None 

Required Data: None

Description: Returns a list of all comments across all reviews as well as the review title that each comment is associated with for added context, example below: 

![GET ALL COMMENTS](https://i.imgur.com/WdpFNz8.jpg)

## Route: /comments/user/\<int:user_id>
HTTP Request verb: GET

Arguments: Integer of the user_id belonging to the user whose comments are to be retrieved.

Authentication: None

Required Data: None

Description: Returns a list of all the comments by the specified user. If no such user exists with a user_id matching the specified user_id an error will be displayed, example below: 

![GET COMMENTS FOR USER NOT FOUND](https://i.imgur.com/tRIBJes.jpg) 

If a user has not made any comments then an error message will be displayed, example below: 

![GET COMMENTS FOR USER NO COMMENTS](https://i.imgur.com/u8tesmm.jpg)

If a user exists with a user_id matching the specified user_id all the comments by that user will be returned, example below: 

![GET COMMENTS FOR USER SUCCESS](https://i.imgur.com/Q6eVBQh.jpg) 

## Route: /comments/review/\<int:review_id>
HTTP Request verb: GET

Arguments: Integer of the review_id beloning to the review whose comments are to be retrieved. 

Authentication: None

Required Data: None

Description: Returns a list of all the comments for a specific review. If no such review exists with a review_id matching the specified review_id an error will be displayed, example below: 

![GET ALL COMMENTS FOR REVIEW NO REVIEW FOUND](https://i.imgur.com/wxCuUVy.jpg) 

If a review does not have any comments on it then an error message will be displayed, example below: 

![GET COMMENTS FOR REVIEW NO COMMENTS](https://i.imgur.com/kHor6zQ.jpg)

If a review exists with a review_id matching the specified review_id and the review has comments on it, then a list of all those comments will be returned, example below: 

![GET COMMENTS FOR REVIEW SUCCESS](https://i.imgur.com/Ce5eStj.jpg)

## Route: /comments
HTTP Request verb: POST

Arguments: None

Authentication: Users need to be authenticated with their access token before creating comments 

Required Data: Body, Review_ID

Description: Allows users to create a new comment on a review. If no review exists with a review_id matching the review_id provided in the request an error will be displayed, example below: 

![POST COMMENT NO REVIEW ID](https://i.imgur.com/CZaml9d.jpg) 

If a comment is posted without a required field, or with a field that is not required, an error message will be displayed, example below: 

![POST COMMENT FIELDS](https://i.imgur.com/lVNlSuH.jpg)

If the required fields are supplied and a review exists matching the supplied review_id the freshly made comment will be returned, example below: 

![POST COMMENT SUCCESS](https://i.imgur.com/vXKI4zN.jpg)

## Route: /comments/\<int:comment_id>
HTTP Request verb: PUT, PATCH

Arguments: Integer of the comment_id for the comment to be updated.

Authentication: Users need to be authenticated with their access token and be authorised to update the comment by either being an admin or the owner of the comment. 

Required Data: BODY

Description: Allows users to update the body content of a comment.If no such comment exists with a comment_id matching the specified comment_id an error message will be displayed. 

![PUT COMMENT NOT FOUND](https://i.imgur.com/rwX1Xo7.jpg) 

If a user is not authorized to update the comment, an error message will be displayed, example below: 

![PUT COMMENT NOT ADMIN](https://i.imgur.com/coVeKAc.jpg) 

If a comment exists with a comment_id matching the specified comment_id and the user is authroised to update the comment, the freshly updated comment will be returned, example below: 

![PUT COMMENT SUCCESS](https://i.imgur.com/B4a2k2y.jpg) 

## Route: /comments/\<int:comment_id>
HTTP Request verb: DELETE

Arguments: Integer of the comment_id for the comment to be updated.

Authentication: Users need to be authenticated with their access token and be authorised to delete the comment by either being an admin or the owner of the comment. 

Required Data: None

Description: Allows comment owners or admins to delete a comment. If no such comment exists with a comment_id matching the specified comment_id an error message will be displayed, example below: 

![DELETE COMMENT NOT FOUND](https://i.imgur.com/ImLM641.jpg) 

If a user is not authorised to delete the comment, an error message will be displayed, example below: 

![DELETE COMMENT NOT ADMIN](https://i.imgur.com/3jD5Vt6.jpg) 

If a comment exists with a comment_id matching the specified comment_id and the user is authorised to delete the comment, a confirmation message will be displayed, example below: 

![COMMENT DELETE SUCCESSFUL](https://i.imgur.com/VICkpiv.jpg)

