#include "ofApp.h"
#include "ofxCv.h"
#include "ofBitmapFont.h"


void ofApp::drawMarker(float size, const ofColor & color){
    if(drawAxis){
        ofDrawAxis(size);
    }
    //To prevent from fucking up the other parts of the world
    ofPushMatrix();
    // move up from the center by size*.5
    // to draw a box centered at that point
    ofTranslate(0,size*0.5,0);
    
    
    //Gui
    ofRotateX(rotateX);
    ofRotateY(rotateY);
    ofRotateZ(rotateZ);
    
//    swtich statment takes current scene
//    switch(currentScene){ case: 1 renderfirstscene(); break;
//    switch(currentScene) {
//        case 1 : cout << 'the first scene is rendering' << endl; // prints "1"
//            //call the function to render scene
//            break;       // and exits the switch
//        case 2 : cout << '2';
//            break;
//    }
    
    //Esxample scene
    ofFill();
    ofSetColor(color,50);
    ofDrawBox(size);
    ofNoFill();
//    if(bammm < 361){
//        bammm++;
//    } else {
//        bammm = 0;
//    }
    ofRotateY(bammm);
    ofSetColor(color);
    ofDrawBox(size);
    
    //we like pop prevent from fucking up the other parts of the world
    ofPopMatrix();
}

void ofApp::drawCube(float size, const ofColor & color){
    if(drawAxis){
        ofDrawAxis(size);
    }

    ofPushMatrix();
    ofTranslate(positionX,size*0.5,0);
    
    //Gui
    ofRotateX(rotateX);
    ofRotateY(rotateY);
    ofRotateZ(rotateZ);

    ofFill();
    ofSetColor(color,50);
    ofDrawBox(size);
    ofPopMatrix();
}

void ofApp::drawSphere(float radius, const ofColor & color){
    if(drawAxis){
        ofDrawAxis(radius);
    }
    
    ofPushMatrix();
    
    //Gui
    ofRotateX(rotateX);
    ofRotateY(rotateY);
    ofRotateZ(rotateZ);
    
    ofFill();
    ofSetColor(ofColor::red,50);
    ofDrawSphere(0.0, 0.0, radius);
    ofNoFill();
    ofSetColor(color);
    ofDrawSphere(0.0, 0.0, radius);
    ofPopMatrix();
}

//--------------------------------------------------------------
void ofApp::setup(){
    //shape animation
//    bammm = 0;
    
    drawAxis = false;
    ofSetVerticalSync(true);
    useVideo = false;
    
    //gui
    gui.setup();
    gui.add(rotateX.setup("Rotate X", 0, 0, 360));
    gui.add(rotateY.setup("Rotate Y", 0, 0, 360));
    gui.add(rotateZ.setup("Rotate Z", 0, 0, 360));
    gui.add(positionX.setup("Position X", 0, -1, 1));
    gui.add(drawAxis.setup("Helper Axis", false));
    
    //AR stuff
    string boardName = "boardConfiguration.yml";
    grabber.listDevices();
    grabber.setDeviceID(1);
    grabber.initGrabber(1280,720);
    video = &grabber;
    
    //aruco.setThreaded(false);
    aruco.setup("intrinsics.int", video->getWidth(), video->getHeight(), boardName);
    aruco.getBoardImage(board.getPixels());
    board.update();
    
    showMarkers = true;
    showBoard = true;
    showBoardImage = false;
    
    ofEnableAlphaBlending();
    
}

//--------------------------------------------------------------
void ofApp::update(){
    video->update();
    if(video->isFrameNew()){
        aruco.detectBoards(video->getPixels());
    }
}

//--------------------------------------------------------------
void ofApp::draw(){
    ofSetColor(255);
    video->draw(0,0);
    //aruco.draw();
    
    if(showMarkers){
        for(int i=0;i<aruco.getNumMarkers();i++){
            aruco.begin(i);
//            drawMarker(0.15,ofColor::white);
            aruco.end();
            ofDrawBitmapString("markers ID " + ofToString(aruco.getMarkers()[i].idMarker),500,20);
            
        }
    }
    
    if(showBoard && aruco.getBoardProbability()>0.03){
        for(int i=0;i<aruco.getNumBoards();i++){
            if(aruco.getMarkers()[i].idMarker == 299) {
                aruco.beginBoard(i);
                drawSphere(.2,ofColor::red);
                aruco.end();
            } else {
                aruco.beginBoard(i);
                drawCube(.2,ofColor::aliceBlue);
                aruco.end();
            }
            
        }
    }
    
    
    ofSetColor(255);
    if(showBoardImage){
        board.draw(ofGetWidth()-320,0,320,320*float(board.getHeight())/float(board.getWidth()));
    }
    
    ofDrawBitmapString("markers detected: " + ofToString(aruco.getNumMarkers()),20,20);
    ofDrawBitmapString("fps " + ofToString(ofGetFrameRate()),20,40);
    ofDrawBitmapString("m toggles markers",20,60);
    ofDrawBitmapString("b toggles board",20,80);
    ofDrawBitmapString("i toggles board image",20,100);
    ofDrawBitmapString("s saves board image",20,120);
    ofDrawBitmapString("0-9 saves marker image",20,140);
    
    gui.draw();
}

//--------------------------------------------------------------
void ofApp::keyPressed(int key){
    if(key=='m') showMarkers = !showMarkers;
    if(key=='b') showBoard = !showBoard;
    if(key=='i') showBoardImage = !showBoardImage;
    if(key=='s') board.save("boardimage.png");
    if(key>='0' && key<='9'){
        // there's 1024 different markers
        int markerID = key - '0';
        aruco.getMarkerImage(markerID,240,marker);
        marker.save("marker"+ofToString(markerID)+".png");
    }
}

//--------------------------------------------------------------
void ofApp::keyReleased(int key){
    
}

//--------------------------------------------------------------
void ofApp::mouseMoved(int x, int y ){
    
}

//--------------------------------------------------------------
void ofApp::mouseDragged(int x, int y, int button){
    
}

//--------------------------------------------------------------
void ofApp::mousePressed(int x, int y, int button){
    ofLog() << "The position of the mouse is at " << x << " and y is at " << y << endl;
}

//--------------------------------------------------------------
void ofApp::mouseReleased(int x, int y, int button){
    
}

//--------------------------------------------------------------
void ofApp::windowResized(int w, int h){
    grabber.initGrabber(w,h);
}

//--------------------------------------------------------------
void ofApp::gotMessage(ofMessage msg){
    
}

//--------------------------------------------------------------
void ofApp::dragEvent(ofDragInfo dragInfo){
    
}
