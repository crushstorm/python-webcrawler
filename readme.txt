How to run : 
python metaextract.py 'http://www.cnn.com/2013/06/10/politics/edward-snowden-profile/'


Dependencies : 
beautifulsoup4
To install: pip install beautifulsoup4

Approach:
My approach is to fully utilize the presence of metadata information of the webpage. All the webpages typically contain the metadata description. 

In python, I use the HTML parser called beautifulsoup, which is identically almost same as Jsoup. 

By using regex on the HTML results, I was able to find various keywords that describes the websites. 

We store everything in the set tuple in order to remove duplicates/redundancies

Sample :

http://www.amazon.com/Cuisinart-CPT-122-Compact-2-Slice-Toaster/dp/B009GQ034C/ref=sr_1_1?s=kitchen&ie=UTF8&qid=1431620315&sr=1-1&keywords=toaster
Relevant keywords : 
Cuisinart
save up to 50%.
CPT-122
Amazon.com: Cuisinart CPT-122 Compact 2-Slice Toaster: Kitchen & Dining
Shop Cuisinart at the Amazon Kitchen Small Appliances store. Free Shipping on eligible items. Everyday low prices
Cuisinart CPT-122 Compact 2-Slice Toaster

http://blog.rei.com/camp/how-to-introduce-your-indoorsy-friend-to-the-outdoors/
Relevant keywords : 
Take the Lead
Share your passion for the outdoors and introduce a friend to hike and camp--don't forget to start slow.
Keep Pace with Your Friend
Think Small
Keep it Up
Extend an Invitation

http://www.cnn.com/2013/06/10/politics/edward-snowden-profile/
Relevant keywords : 
Man behind NSA leaks says he did it to safeguard privacy
politics
liberty - CNNPolitics.com
Edward Snowden might never live in the U.S. as a free man again after leaking secrets about a U.S. surveillance program

http://www.alibaba.com
Relevant keywords : 
Buyers
Exporter
Manufacturers
Suppliers
Importer
Wholesalers
Trade Leads
Find quality Manufacturers
Importers
Supplier
Products
Products and Trade Leads from our award-winning International Trade Site. Import & Export on alibaba.com
Exporters
Manufacturer

http://www.spotify.com
Relevant keywords : 
album
Spotify
play
artist
Spotify is a digital music service that gives you access to millions of songs.
digital
playlist
streaming
music
online
listen