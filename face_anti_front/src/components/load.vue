<script setup lang="ts">
import {ref} from "vue";
import { Plus } from '@element-plus/icons-vue'
import {UploadOne} from '@icon-park/vue-next'
import instance from "@/service";
const mind_src=ref('')
const video_src=ref('')
const image = ref({
  name:'',
  url:''
})
const video_obj = ref({
  name:'',
  url:''
})
const email = ref({
  email:localStorage.getItem("email")
})
function handleExceed(){
  alert("一次只能上传一张图片进行分析")
}
interface ImageValue{
  filename: string;
  url: string;
}

function handleSuccess(res:ImageValue){
  alert("上传成功")
  console.log(res)
  image.value.url='/api'+res.url
  image.value.name = res.filename
  console.log(image.value)
}
function handleSuccess_video(res:ImageValue){
  alert("上传成功")
  console.log(res)
  video_obj.value.url='/api'+res.url
  video_obj.value.name = res.filename
  console.log(video_obj.value)
}
function handleFailure(){
  alert("上传失败")
}
function picture_analysis(){
  instance.post(
    '/analysis_picture',
    {'email':email.value.email,'filename':image.value.name}
  ).then((res)=>{
    console.log(res)
    mind_src.value='/api'+res.image_path
  })
}
function vedio_analysis(){
  instance.post(
    '/analysis_video',
    {'email':email.value.email,'filename':video_obj.value.name}
  ).then((res)=>{
    console.log(res)
    video_src.value='/api'+res.video_path
  })
}


</script>

<template>
  <div style="display: flex">
    <div class="left_box">
      <div>
        <upload-one style="vertical-align:bottom " theme="filled" size="30" fill="#030000" :strokeWidth="2" strokeLinecap="square"/>
        <h2 style="display: inline;margin-left: 10px">图片上传</h2>
      </div>
      <br/>
      <div class="load_in">
        <el-upload
            class="avatar-uploader"
            action="/api/uploadimg"
            :limit="1"
            :on-exceed="handleExceed"
            :on-success="handleSuccess"
            :on-error="handleFailure"
            :data="email"
        >
          <el-icon class="avatar-uploader-icon"><Plus /></el-icon>
        </el-upload>
        <el-button type="primary" class="submit_picture" @click="picture_analysis"> 图片分析</el-button>
      </div> 
      <h5 class="tip">说明：上传成功后，点击图片分析即可查看分析结果</h5>
      <h5 v-if="mind_src!==''">{{'analysis_'+image.name }}</h5>
      <div v-if="mind_src!==''" class = "load_out">
        <el-image class="picture" :src="mind_src" :preview-src-list="[mind_src]" preview-teleported/>
      </div>
    </div>
    <div class="right_box">
      <div>
        <upload-one style="vertical-align:bottom " theme="filled" size="30" fill="#030000" :strokeWidth="2" strokeLinecap="square"/>
        <h2 style="display: inline;margin-left: 10px">视频上传</h2>
      </div>
      <h5 class="tip">说明：要求尺寸最好是小于1GB格式为MP4</h5>
      <div class="load_in">
        <el-upload
            class="avatar-uploader"
            action="/api/upload_video"
            :limit="1"
            :on-exceed="handleExceed"
            :on-success="handleSuccess_video"
            :on-error="handleFailure"
            :data="email"
        >
          <el-icon class="avatar-uploader-icon"><Plus /></el-icon>
        </el-upload>
        <el-button type="primary" class="submit_picture" @click="vedio_analysis"> 视频分析</el-button>
      </div>
      <br/>
      <h5 class="tip">说明：上传成功后，点击视频分析即可查看分析结果</h5>
      <div class = "load_out" v-if="video_src==''">
        <span>请等待...</span>
        <el-icon><Loading /></el-icon>
      </div>
      <div class = "load_out" v-if="video_src!==''">
        <video controls autoplay width="100%" class="video" name="media">
          <source :src="video_src" type="video/mp4"/>
        </video>
      </div>
    </div>
  </div>

</template>

<style scoped>
.left_box{
  background-color: azure;
  height: 95vh;
  width: 76vh;
  padding: 10px;
}
.el-icon.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 178px;
  height: 178px;
  text-align: center;
  border: dashed black 1px;
  border-radius: 10px;
}
.submit_picture{
  float: right;
}
.avatar{
  margin-left: 10px;
}
.right_box{
  margin-left: 2vh;
  width: 40vw;
}
.load_out{
  text-align: center;
  
}
.picture{
  max-width: 30vw;

  border-radius: 10px;
}
.vedio{
  max-width: 40vw;
  max-height:50vh;
  border-radius: 10px;
}
</style>