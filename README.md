# cap-bot <img align="right" height="60" src="gui/assets/logo.png">
 [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) <br/>
A one stop GUI to provide multiple Image-Captioning application with ease and efficiency.
## Motivation
With the rise of automated transportation there has arisen a need of having some kind of logging system for the vehicle to describe the surroundings in case of accidents. We here are aiming to make a GUI which will be able to take in input from an external camera and perform image captioning on it to save it in logs in case of such incidents and give the owners a better understanding of any kind of damage or loss in their automated vehicle. 
Our secondary features inlvolve implementing the same kind of system for CCTV cameras to make incident mapping easy by using keywords to jump to time frames from the log.
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
- [.] Making GUI using HTML CSS .
- [.] Add a python script to tap into external camera.
- [.] Finishing the Image Captioning Model.
- [ ] Make the Search Module.
- [ ] Sort the backend.
- [ ] Add some ease of access methods.(secondary)
## License 
This project is under the Apache License. See [LICENSE](LICENSE) for Details.
