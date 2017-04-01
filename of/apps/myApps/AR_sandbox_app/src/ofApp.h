#pragma once

#include "ofMain.h"
#include "ofxAruco.h"
#include "ofxGui.h"


class ofApp : public ofBaseApp{
    
public:
    void setup();
    void update();
    void draw();
    
    void keyPressed  (int key);
    void keyReleased(int key);
    void mouseMoved(int x, int y );
    void mouseDragged(int x, int y, int button);
    void mousePressed(int x, int y, int button);
    void mouseReleased(int x, int y, int button);
    void windowResized(int w, int h);
    void dragEvent(ofDragInfo dragInfo);
    void gotMessage(ofMessage msg);
    
    void drawMarker(float size, const ofColor & color);
    void drawCube(float size, const ofColor & color);
    void drawSphere(float size, const ofColor & color);
    
    
    ofVideoGrabber grabber;
    ofVideoPlayer player;
    
    ofBaseVideoDraws * video;
    
    ofxAruco aruco;
    bool useVideo;
    bool showMarkers;
    bool showBoard;
    bool showBoardImage;
    ofImage board;
    ofImage marker;
    
    ofxPanel gui;
    ofxFloatSlider rotateX;
    ofxFloatSlider rotateY;
    ofxFloatSlider rotateZ;
    ofxFloatSlider positionX;
    ofxToggle drawAxis;
    
    float bammm;
    
    int currentScene;
    
};
