<!-- eslint-disable vue/multi-word-component-names -->
<template>
<div class="container">
    <div class="box">
        <h5 class="tip">历史图片数据</h5>
        <br/>
        <br/>
        <br/>
        <div class="left">
            <el-card shadow="hover" class="list_button" v-for="(item,index) in history_picture_list" :key="index">
                <template #header>{{ item.name }}</template>
                <el-image  :preview-src-list="[item.url]" :src="item.url" alt=""/>
                <br/>
                <div class="button_list">
                    <el-button class="button" type="primary">开始分析</el-button>
                    <el-button class="button" type="danger">删除</el-button>
                </div>
                
            </el-card>
        </div>
    </div>
        <div class="box">
            <h5 class="tip">图片结果数据</h5>
            <br/>
            <br/>
            <br/>
            <div class="middle_left">
                <el-card shadow="hover" class="list_button" v-for="(item,index) in result_picture_list" :key="index">
                    <template #header>{{ item.name }}</template>
                    <el-image  :preview-src-list="[item.url]" :src="item.url" alt=""/>
                    <br/>
                    <div class="button_list">

                        <el-button class="button" type="danger">删除</el-button>
                    </div>
                    
            </el-card>
        </div>
    </div>
</div>
</template>

<script setup>
import instance from '@/service';
import {useRouter} from 'vue-router'
import {reactive, ref,onMounted} from 'vue';

const router = useRouter()
onMounted(()=>{
    const formData = new FormData()
    const email = localStorage.getItem('email')
    if(email == null){
        console.log("未登录")
        router.push('./login')
        return
    }
    let images = []
    let analysis_images = []
    formData.append('email',email)
    instance.post('/get_images',formData).then((res)=>{
        images = res.img === undefined ? [] : res.img
        analysis_images = res.analysis_img === undefined ? [] : res.analysis_img
        for(let i = 0;i<images.length;i++){
            history_picture_list.push({
                name:images[i].name,
                url:'/api/'+images[i].url
            })
        }
        for(let i = 0;i<analysis_images.length;i++){
            result_picture_list.push({
                name:analysis_images[i].name,
                url:'/api/'+analysis_images[i].url
            })
        }
    })
})
const history_picture_list = reactive([])
const result_picture_list = reactive([])
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
.left{
    background-color:  azure;
    display: flex;
    flex-flow: row wrap;
    justify-content: flex-start;
}
.middle_left{
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