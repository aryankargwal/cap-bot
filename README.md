# cap-bot||Team Missing Colon <img align="right" height="60" src="gui/assets/logo.png"><br/>
 [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
 [![GitHub commits](https://img.shields.io/github/commits-since/Naereen/StrapDown.js/v1.0.0.svg)](https://github.com/aryankargwal/cap-bot/commit/)
 [![GitHub contributors](https://img.shields.io/github/contributors/Naereen/StrapDown.js.svg)](https://github.com/aryankargwal/cap-bot/graphs/contributors/)
 <br/>
## Problem Statement
***‘OH NO! Where is my laptop?? Who stole it??’***<br/>
***‘Bro don't worry go to the warden he will help you with the CCTV Footage.’***<br/>
Now or then you might have found yourself in a situation where you get your *life* essentials stolen and are directed to your CCTV operator but this can be a huge hassle when you belong to colleges with ***Huge*** Campuses. Now you can do the foolish thing by checking the hundreds of hours of footage through the dozens of cameras or you can use our ***Project***!!

## Solution
We present you ***cap-bot***, a deskptop app capable of running Image Captioning on multiple CCTV camera footages around huge enterprises and storing the said captions in a convenient log.<br/>
***Image Captioning***, the new and hip way of understanding images!! Its being used in Automative Vehicles! Its being used by ***GOOGLE***! Its being used in ***FACEBOOK***! But, now we use it here in our own beloved project ***cap-bot***. Image Captioning enables us to capture various details in a picture and put them in a sentance which can be used in Autonomous Vehicle's logging modules, reverse image searches and much more.<br/>
We here are implementing an Image Captioning model working on the ***VGG-16*** Network which we trained on the ***Flickr8K*** dataset, which gets its images from an OpenCV module that we would have ideally preferred to work on a ***Key Event Detection*** system but have it working on a ***Time-Period System***.<br/>
Now once we have the captions we store them in a database using ***Pandas*** where we have cleverly used the corpus ids of the words so as to ease the search process.

## Exploring GUI


## Running the App
Firstly, let us enter the folder for the GUI.
```
cd gui
```
Now, we will install the node modules which are listed in the package.json using
```
npm install
```
Now. we can finally run the app using
```
npm start
```

## Steps for Development
- [x] Making GUI using HTML CSS .
- [x] Add a python script to tap into external camera.
- [x] Finishing the Image Captioning Model.
- [x] Make the Search Module.
- [ ] Sort the backend.
## License 
This project is under the Apache License. See [LICENSE](LICENSE) for Details.
## Authors
<table>
  <tr>
       <td align="center"><a href="https://github.com/AnanyaNegi"><img src="/images/ananya.jpeg" width="210px;" height="230px;" alt=""/><br /><sub><b>Aryan Kargwal</b></sub></a><br /><p align="center">
    
   <a href="https://www.linkedin.com/in/ananya-negi-42922018a" alt="Linkedin"><img src="https://raw.githubusercontent.com/jayehernandez/jayehernandez/3f5402efef9a0ae89211a6e04609558e862ca616/readme/linkedin-fill.svg"></a>
  </p>
</td>
      
   <td align="center"><a href="https://github.com/yadvi12"><img src="https://media-exp1.licdn.com/dms/image/C5603AQFCctkhnahzoA/profile-displayphoto-shrink_800_800/0?e=1611792000&v=beta&t=BUN04pA5DksAkUe8EhpCPGoSe3PFuETyzpIz8KMhZbA" width="270px;" height="230px;" alt=""/><br /><sub><b>Srijarko Roy</b></sub></a><br />
    <p align="center">
   
   <a href="https://www.linkedin.com/in/srijarko-roy-9193751b0/" alt="Linkedin"><img src="https://raw.githubusercontent.com/jayehernandez/jayehernandez/3f5402efef9a0ae89211a6e04609558e862ca616/readme/linkedin-fill.svg"></a>
  </p>

</td>
   
   <td align="center"><a href="https://github.com/Reeti1605"><img src="/images/WhatsApp Image 2020-10-09 at 1.25.32 PM.jpeg" width="210px;" height="230px;"  alt=""/><br /><sub><b>Indira Dutta</b></sub></a><br />
<p align="center">
    
   <a href="https://www.linkedin.com/in/reeti-jha-9672691b4/" alt="Linkedin"><img src="https://raw.githubusercontent.com/jayehernandez/jayehernandez/3f5402efef9a0ae89211a6e04609558e862ca616/readme/linkedin-fill.svg"></a>
  </p>
</td>
   
   <td align="center"><a href="https://github.com/ampsteric"><img src="/images/shashwat.png" width="240px"; height="230px;" alt=""/><br /><sub><b>Kunal Mundada</b></sub></a><br />
<p align="center">
   
   <a href="https://www.linkedin.com/in/shashwat-mishra-699bab194/" alt="Linkedin"><img src="https://raw.githubusercontent.com/jayehernandez/jayehernandez/3f5402efef9a0ae89211a6e04609558e862ca616/readme/linkedin-fill.svg"></a>
  </p>
</td>
    </tr>
    </table>

