import { View, Text, Image, ImageBackground, ScrollView, Button, Pressable, Modal } from 'react-native';
import { useState } from 'react';

/*import img from assets folder*/
const logoImg = require("./assets/android-icon-monochrome.png");

export default function App() {
  const [isModalVisible, setIsModalVisible] = useState(false);
  return (
    <View style={{flex: 1, backgroundColor: "plum", padding: 60}}>
      <Button title="Press" onPress={() => console.log("Button pressed.")} color="midnightblue" disabled />
      <Pressable onPress={() => setIsModalVisible(true)}>
        <Image source={logoImg} style={{width: 300, height: 300}}/> 
      </Pressable>
      {/* scrollview */}
      <ScrollView>
        <View style={{width: 200, height: 200, backgroundColor: "lightblue"}}></View>
        <View style={{width: 200, height: 200, backgroundColor: "lightgreen"}}></View>
        <Text>
          <Text style={{color: "white"}}>Hello</Text>World!
        </Text>
          <Image source={logoImg} style={{width: 300, height: 300}}/> 
          <Image source={{uri: "https://picsum.photos/seed/picsum/300"}} style={{width: 300, height: 300}}/> 
          <ImageBackground source={logoImg} style={{flex: 1}}>
            <Text>IMAGE TEXT</Text>
          </ImageBackground>
          <Text>
            Here is some more text yayayay. 
          </Text>
          <Image source={logoImg} style={{width: 300, height: 300}}/> 
        </ScrollView>
        <Modal visible={isModalVisible} onRequestClose={() => setIsModalVisible(false)}
            animationType="slide" presentationStyle='fullScreen'>
              <View style={{flex: 1, backgroundColor: "pink", padding: 60}}>
                <Text>Modal content</Text>
                <Button title="Close" color="midnightblue" onPress={() => setIsModalVisible(false)}/>
              </View>
        </Modal>
    </View>
  );
}


