<!-- eslint-disable vue/multi-word-component-names -->
<template>
<div class="container">
    <div class="box">
        <h5 class="tip">历史视频数据</h5>
        <br/>
        <br/>
        <br/>
        <div class="middle_right">
            <el-card shadow="hover" class="list_button" v-for="(item,index) in history_video_list" :key="index">
                <template #header>{{ item.name }}</template>
                <video ref="video" :src="item.url" width="300" height="200"></video>
                <br/>
                <div class="button_list">
                    <el-button class="button" type="primary" @click="showDetail(item.url)">查看详情</el-button>
                    <el-button class="button" type="primary">开始分析</el-button>
                    <el-button class="button" type="danger">删除</el-button>
                </div>
            </el-card>
        </div>
    </div>
    <div class="box">
        <h5 class="tip">视频结果数据</h5>
        <br/>
        <br/>
        <br/>
        <div class="right">
            <el-card shadow="hover" class="list_button" v-for="(item,index) in result_video_list" :key="index">
                <template #header>{{ item.name }}</template>
                <video  :src="item.url" width="300" height="200"></video>
                <br/>
                <div class="button_list">
                    <el-button class="button" type="primary" @click="showDetail(item.url)">查看详情</el-button>
                    <el-button class="button" type="danger">删除</el-button>
                </div>
            </el-card>
        </div>
    </div>
</div>
</template>

<script setup>
import {ref,onMounted} from 'vue';
import instance from '@/service';
import { useRouter } from 'vue-router';
const router = useRouter()
const video = ref(null)
onMounted(()=>{
    const formData = new FormData()
    const email = localStorage.getItem('email')
    if(email == null){
        console.log("未登录")
        router.push('./login')
        return
    }
    let video = []
    let analysis_video = []
    formData.append('email',email)
    instance.post('/get_videos',formData).then((res)=>{
        video = res.video === undefined ? [] : res.video
        analysis_video = res.analysis_video === undefined ? [] : res.analysis_video
        for(let i = 0;i<video.length;i++){
            history_video_list.value.push({
                name:video[i].name,
                url:'/api'+video[i].url
            })
        }
        for(let i = 0;i<analysis_video.length;i++){
            result_video_list.value.push({
                name:analysis_video[i].name,
                url:'/api'+analysis_video[i].url
            })
        }
        console.log(result_video_list.value)
    })
})
const history_video_list = ref([])
const result_video_list = ref([])
function showDetail(url){
    window.open(url,'_blank')
}
</script>

<style scoped lang="scss">
.container{
    display: flex;
}
.box{
    width: 42vw;
    max-height: 98vh;
    margin-right: 0.1vw;
    overflow: auto;
    min-height: 98vh;
}
.middle_right{
    background-color:  azure;
    display: flex;
    flex-flow: row wrap;
    justify-content: flex-start;
}
.right{
    background-color: white;
    display: flex;
    flex-flow: row wrap;
    justify-content: flex-start;
}
.tip{
    position: fixed;
    z-index: 100;
    width:37.5vw;
    background-color: rgb(221, 219, 219);
    padding: 20px;
    margin-top: 0.0vh;
    border-radius: 10px;
}
.list_button{
    margin-top: 6px;
    width: 20vw;
    max-height: 400px;
}
img{
    width: 100%;
}
.button{
    width: 100%;
}
.button_list{
    display: flex;
    flex-direction: row;
}
</style>