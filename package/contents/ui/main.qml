import QtQuick
import QtMultimedia
import org.kde.plasma.wallpapers

Item {
    id: root
    
    // This is the background layer
    Rectangle {
        anchors.fill: parent
        color: "black"
    }

    VideoOutput {
        id: videoOutput
        anchors.fill: parent
        fillMode: VideoOutput.PreserveAspectCrop
        
        MediaPlayer {
            id: player
            videoOutput: videoOutput
            loops: MediaPlayer.Infinite
            // We are hardcoding your specific path for this "John-Edition" build
            source: "file:///home/john/Pictures/Wallpapers/sonic.mp4"
            autoPlay: true
            
            // Mute by default to be safe, we can add a toggle later
            audioOutput: AudioOutput {
                muted: true
            }
        }
    }
}
