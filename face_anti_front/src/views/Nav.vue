/* eslint-disable */

<script setup lang="ts">
import {ref} from "vue";
import {useRouter} from "vue-router";
import {UploadWeb,FindOne,Detection,Logout,Me,ChartPieOne} from '@icon-park/vue-next'
const route = useRouter()
const activeIndex = ref('home')
function handleSelect(key:string,keypath:string[]){
  route.push('/'+key)
  activeIndex.value = key
}
const squareUrl = ref(
    'https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png'
)
</script>

<template>
  <div class="main_box">
    <div class="menu">
      <el-menu :default-active="activeIndex" class="el-menu-demo" mode="vertical" @select="handleSelect">
        <el-menu-item index="home"  class="menu_item">
          <div class="box">
            <span style="color: black;font-size: 15px;">人脸反欺诈技术的研究与应用</span>
          </div>
        </el-menu-item>
        <el-menu-item index="login"  class="menu_item">
          <me theme="filled" size="30" fill="#fdfdfd" :strokeWidth="2" strokeLinecap="square"/>
          <span>登录</span>
        </el-menu-item>
        <el-menu-item index="load"  class="menu_item" >
          <upload-web theme="filled" size="30" fill="#fdfdfd" :strokeWidth="2" strokeLinecap="square"/>
          <span>数据导入</span>
        </el-menu-item>
        <el-menu-item index="datasetPicture"  class="menu_item" >
          <chart-pie-one theme="outline" size="30" fill="#fdfdfd" :strokeWidth="2" strokeLinecap="square"/>
          <span>图片数据</span>
        </el-menu-item>
        <el-menu-item index="datasetVedio"  class="menu_item" >
          <chart-pie-one theme="outline" size="30" fill="#fdfdfd" :strokeWidth="2" strokeLinecap="square"/>
          <span>视频数据</span>
        </el-menu-item>
        <el-menu-item index="onlineAlaysis"  class="menu_item">
          <find-one theme="filled" size="30" fill="#fdfdfd" :strokeWidth="2" strokeLinecap="square"/>
          <span>实时检测</span>
        </el-menu-item>
        <el-menu-item index="setting"  class="menu_item">
          <detection theme="filled" size="30" fill="#fdfdfd" :strokeWidth="2" strokeLinecap="square"/>
          <span>设置</span>
        </el-menu-item>
        <el-menu-item index="7"  class="menu_item">
          <logout theme="filled" size="30" fill="#fdfdfd" :strokeWidth="2" strokeLinecap="square"/>
          <span>退出</span>
        </el-menu-item>
      </el-menu>
    </div>

    <div class="sub_box">
      <router-view />
    </div>

  </div>
</template>

<style scoped lang="scss">
.main_box{
  display: flex;
}
.menu{
  
  background-color: #6493ae;
  height: 98vh;
}
.el-menu-demo{
  padding: 0;
  background-color: transparent;
  .el-menu-item:hover{
    background-color: transparent !important; /* 取消背景色 */
    color: inherit !important; /* 使用继承的颜色 */
  }
}
.menu_item{
  color: white;
}
.box{
  display: flex;
  margin: 0;
  
  padding: 0;
}
.sub_box{
}
span{

  
}
</style>