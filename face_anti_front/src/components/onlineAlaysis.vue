<template>
 <div class="container">
    
    <div style="display: flex;flex-direction: row;">
        <div>
            <video  src="" ref="video" id="video"></video>
            <canvas id="camera"></canvas>
        </div>
        <div>
            <canvas id="camera_result"></canvas>
        </div>
        
    </div>
    <div class="botton_box">
        <el-button type="primary" @click="getCamera()">打开摄像头</el-button>
        <el-button type="danger" @click="closeCamera()">关闭摄像头</el-button>
        <el-button type="primary" @click="getDetection()">开始检测</el-button>
        <el-button type="danger" @click="closeDetection()">关闭检测</el-button>
        <el-button type="primary" @click="function(){}">保存截图</el-button>
        
    </div>
    
 </div>
</template>

<script setup>
import instance from '@/service';
import {ref,onMounted,onBeforeUnmount,} from 'vue';
const video = ref()
const video_result = ref()
let flag = 0
const canvas = ref()
const canvas_result = ref()
const ctx = ref()
const socket = new WebSocket('ws://localhost:8888');
onMounted(()=>{
    console.log('正在打开摄像头。。。')
    getCamera()
    //连接后端socket
    connection()
    reconnection()
})
function connection(){
    socket.onopen = ()=>{
        console.log('socket 已打开...')
    }
}
async function reconnection(){
    console.log('Attempting to reconnect...');
    setTimeout(connection(), 3000); // 3秒后尝试重新连接
}
function getCamera(){
    canvas.value = document.getElementById('camera');
    ctx.value = canvas.value.getContext('2d');
    if(navigator.mediaDevices){
        navigator.mediaDevices.getUserMedia({video:true,audio:false}).then((stream)=>{
            video.value.srcObject = stream;
            video.value.play();
            let  mediaRecorder = new MediaRecorder(stream);
            mediaRecorder.ondataavailable = (event) => {
            if (event.data && event.data.size > 0 && flag === 1) {
                const canvas = document.createElement('canvas');
                canvas.width = video.value.videoWidth;
                canvas.height = video.value.videoHeight;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(video.value, 0, 0, canvas.width, canvas.height);
                // 将图像数据编码为 base64 字符串
                const base64ImageData = canvas.toDataURL('image/jpeg');
                // 发送 base64 编码后的图像数据给后端处理
                //如果socket连接后才开始发送
                socket.send(base64ImageData);
            }
    };
            mediaRecorder.start(33);
        }).catch((err)=>{
            console.log(err)
        })
    }else{
        //防止浏览器版本旧不支持mediaDevices
        navigator.mediaDevices={}
    }
}
onBeforeUnmount(()=>{
    //closeCamera();
})
function closeCamera(){
    let stream = video.value.srcObject;
    if (!stream) return;
    let tracks = stream.getTracks();
    tracks.forEach((x) => {
    x.stop();
    });
}
function getDetection(){
    flag = 1;
    console.log("开始检测")
    socket.onmessage = (event) => {
    console.log(event.data);
    let imageData = event.data;
    // 检查是否为 Blob 对象
    if (imageData instanceof Blob && document.getElementById('camera_result') !== null) {
        // 解码并显示图片
        const ctx = document.getElementById('camera_result').getContext('2d');
        const canvas_result = document.getElementById('camera_result');
        // 将接收到的 blob 格式的图像数据转换为 URL
        const imageUrl = URL.createObjectURL(imageData);
        const img = new Image();
        img.onload = ()=>{
            // 设置画布的宽度和高度
            canvas_result.width = img.width;
            canvas_result.height = img.height;
            // 绘制图像到画布上
            ctx.drawImage(img, 0, 0);
            // 释放 URL 对象
            URL.revokeObjectURL(imageUrl);
        };
        // 设置图像的 src
        img.src = imageUrl;
    } else {
        console.error("Received data is not a Blob object.");
    }
};
}

function closeDetection(){
    flag = 0;
    console.log("关闭检测")
}

</script>

<style scoped lang="scss">
.container{
    display: flex;
    width: 84vw;
    max-height: 90vh;
    flex-direction: column;
    align-items: center;
    background-color: #f0f0f0;
    padding-top: 1%;
    padding-bottom: 3%;
}
#camera{
    width:0;
    height:0;
    display: none;
}
video , #camera_result{
    width:40vw;
    margin-left: 10px;
}
.botton_box{
    margin-top: 10px;
    display: flex;
    flex-direction: row;
}
</style>