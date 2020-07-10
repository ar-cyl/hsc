# hsc
Humanitarian Supply Chain-hackathon



#Features:
-Anyone can sign up with verified document issued by government of Nepal.
-Any Nepali national can become a member.
-Once you become a member, you can voluntarily work to collect information of people in danger, check and verify someone’s work from your area and join hands to establish HSC during disaster response and post-disaster stage.
-One has full control over his private information i.e. you can control what information to display at any time but your name, profile picture and at least one contact information (e.g. email/phone/social media) are always visible.
-However, you can never make your identity verification document public.
- Every record in the database gets membership but they are not considered as volunteer. They can access their profile using registered phone number and must verify identity by entering given OTP.
This access can be used to seek help for themselves or update allowed information fields.

What kind of information do we want?
-Daily wage workers
-Labourer
-Homeless / No possession of land or property
-People under extreme poverty

Why them?
-No matter the nature of disaster, they are the ones at high risk.

How to get data?
Phase1: Prototype and testing
-We’ll conduct few field surveys in our locality and add the information gathered into a database.

Phase2: For full scale implementation
-Collaboration with NGOs and INGOs to get access to their survey reports.
-Co-operation with Governmental bodies.
-Most importantly local authorities and local government.

#Information verification:
Phase1: Prototype
	We can assume that every information collected is reliable as each record is checked and verified by door to door survey from our team.

Phase 2: Full scale implementation
	Once the application goes to full scale implementation, based on the address of a particular entry, volunteer members from that area are asked to verify the information. We are interested in particular information such as their economic condition and family’s income source. One can either say yes to the entered information or choose something else from a list of given options. Top three answers are saved which will play a vital role to determine level of priority later on.

				Record Entry Form (Sample)
(For head of the family)
Name:
Address:
    1. Temporary
    2. Permanent
Contact:
    1. Phone
    2. Mobile
Occupation:
Main source of family income:

Family Members:
Name:
Temporary Address:
Occupation:
Relation of family’s head:
Identity verification document: upload

Based of the identity document, which could be any of the following:
    • Citizenship
    • Passport
    • Voter’s ID
    • Birth certificate
Following information must be entered:
ID no.:
Date of Issuance:
Issued by:

Signature of all family members along with their identity card if possible.

How does the system work?
- A post to help a family is generated which is uniquely identified by an automated ID
ID Format : Date – Disaster Type – Location – Post Type (Pending/Approved) - Case Number

Who can generate such posts?
- Any member with some evident proof (image or a short video)
- The victim himself
- If the victim’s record is available, post gets approved immediately. Basically he is posting from his account. 
- If the victim is not in record, post gets approved if at least 5-10 people from that place verify the post.

Post written for someone not in record:
Later when situation calms down this information will be reviewed and verified. If such posts had fake details, people who wrote such posts will have less credibility score i.e. their review and vote will have less weightage. Weightage value is measured between 1-100.

 		Sample of  Post Generating Form:
Name:
Address: Location + entered
Phone number:
Proof : Photo or a short video
Most important things they need : based on priority (maximum 3 ) 

Note: Maximum number of items will change based on the number of days passed since the disaster occurred. As the time passes and situation calms down, people are looking forward to resuming their life so they might need more things for recovery whereas first few days will be a struggle for survival thus most essential things are given priority.

If first three fields match to our database, post immediately approved otherwise left for verification.
Once the post is approved, both posts are considered identical and left upon users to up-vote or down-vote.  The post with considerably large negative response are considered  fake and goes to the trash. 
		

Rules to write a post:
    1. A victim can write only one post in 24 hours for himself.
    2. 24 hour rule applies to all post written for oneself.
    3. Maximum 3 posts can be written for someone in 24 hours. This limit can be extended, based on situation if required.
    4. Even volunteer members can write post for themselves, at the end of the day no one’s life is disaster proof.
    5. Video post cannot exceed 30s.
    6. Maximum 3 images can be attached to a post.
    7. Maximum character allowed 180.
    8. If the post is for someone else, his/her photo is must. The post must show person’s face clearly.

Who can up-vote and down-vote a post?
-You must be signed in, doesn’t matter you are a volunteer or not but must be a member. If your profile doesn’t match with information of the post i.e. you can’t vote or verify your own post or a post liked to your family.


How to define a member’s radius of influence?
-If the origin of post is within certain radius from the permanent address of the member, he/she can vote on a post whereas the radius of influence is determined by multiple factors like population density, metro-city, municipality or village municipal.

		Post Verification Notification (Sample):
Name of effected person
Address: Location of post + from the record or location entered by post generator.
Proof: image or video attached to the post
Post ID: auto generated
You  can up-vote or down-vote by simply clicking the associated button.



For now, let’s assume everything goes as planned, which means we have an application that has enough data, large number of members and they can post for help when disaster hits.

Say,  a  user logged in and found a post urging for help. It was suggested to him based on his location, he happened to have what the victim needed so he decided to help. How will this process go?

He writes a response post  with the ID of the post attached  he records a small clip mentioning the things he is going to provide. The victim mentioned in the post gets a unique password related to this response which will be used later. This means the ID is engaged; an engaged ID gets less priority for next 12 hours. If no help was provided on that thread until next 12 hours, it comes back to priority list. 

For now let’s say that he managed to reach the victim and provide some help.  Now, for verification we will use password generated after he got engaged in this post . For simplicity, we will name the victim ‘A’ and the person who wants to help him ‘B’. There can be two different situations:

    1. Post generated by the victim himself or his family member :  Both A and B will write a new post connecting to the original thread along with the help provided to A. The post won’t be approved until A enters the password from his profile. 
    2. Post generated by someone else: When someone gets engaged on such post, generated password is sent in A’s message box. Once B helps him they write a common post connecting to the original thread and A will enter the password from B’s profile. This entire process will be notified to the person who wrote this post for A.

Post to close engagement/ After receiving help:
Guidelines:
    1. List of things provided.
    2. At maximum 3 photos
    3. At maximum 30s video
    4. Photo and video must show the victim in frame.


Note: 
    1. As soon as someone engages on a post, the ID of the post will be updated to engaged.
    2. A person who engages to a post and doesn’t respond will have less credibility in later activities.
    3. A person with very low credibility might not be able to engage in a post. ( criteria will be decided later)
    4. If a person with low credibility gets engaged with a post, priority of that post won’t decrease significantly. 

What happens to a post once the victim receives help?
-This will decrease the priority level of that post. Naturally some other post with no help gets more priority. 

How to measure priority index?
- It will be measured in a scale of 1-10.
-All unengaged posts have equal priority. A user sees all unengaged posts in the order of his proximity.
-Once a thread is engaged, it gets less priority for next 12 hours.
	First 
		2 hours 		2 points
		5 hours 		4 points
		7 hours 		6 points
		10 hours 		8 points
		12 hours 		10 points
- If the engaged thread receives no help in next 12 hours it is back to the top priority again.
- If the victim gets some help then priority reduces based on the amount of help he got.
	Items got in percent:
				100		0 points 
				80		2 points
				60 		4 points
				40		6 points

				below is considered no help provided as maximum limit is of three items. As the limit of items increase, this indexing scheme will also change accordingly.

How can a member improve his/her credibility?
-Not enough to engage with a post: Only way to improve is by adding new records with correct information. If your entry gets ‘yes’ response, you will earn positive credibility points. 
-Enough to engage with a post but still low : First option is always open for you. Second thing you can do is actually help people and collect positive credit points.
		

“I have assumed that everything goes as planned here, well that is definitely not the case in real world. Disaster itself means a time of complete chaos and everything cannot be planned and it is very difficult to predict human behaviour. ”

			“Things always don’t move in a straight line.”


notes:
help payeko photo public huda na help payeka lai na ramro lagna sakxa k tei vayera dine ra paune le matra dekhna sakne banauna milxa hola ni

data can be collected from ntc, and system acts as part of gov service
