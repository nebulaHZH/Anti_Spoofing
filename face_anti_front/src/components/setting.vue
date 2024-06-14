<!-- eslint-disable vue/multi-word-component-names -->
<template>
 <div class="container">
    <div class="row">
        <h5 class="text-center">模型选择：</h5>
        <el-select v-model="value" placeholder="默认yolov8" style="width: 240px">
            <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value"
            />
        </el-select>
    </div>
    <div class="row">
        <h5 class="text-center">重设密码：</h5>
        <el-input class="input" type="password" placeholder="请输入新密码" v-model="code1" show-password/>
        <h5 class="text-center" style="margin-left:5px;">再次输入：</h5>
        <el-input class="input" type="password" placeholder="确认密码" v-model="code2" show-password/>
        <el-button type="primary" style="margin-left:5px;" @click="modify_code">确定</el-button>
    </div>
    <div class="row">
        <h5 class="text-center">清空所有历史数据：</h5>
        <el-button type="primary" style="margin-left:5px;" @click="dialogVisible = true">确定</el-button>
        <el-dialog
            v-model="dialogVisible"
            title="提示"
            width="500"
            :before-close="handleClose"
        >
            <span>是否删除所有历史数据？</span>
            <template #footer>
            <div class="dialog-footer">
                <el-button @click="dialogVisible = false">取消</el-button>
                <el-button type="primary" @click="dialogVisible = false">
                确定
                </el-button>
            </div>
            </template>
        </el-dialog>
    </div>
 </div>
</template>

<script setup>
import instance from '@/service';
import { ref } from 'vue'
const value = ref('')
const code1 = ref('')
const code2 = ref('')
const dialogVisible = ref(false)
const options = [
  {
    value: 'yoloV8',
    label: 'yoloV8模型',
  },
  {
    value: 'yoloV7',
    label: 'yoloV7模型',
  },
  {
    value: 'faceBagNet',
    label: 'faceBagNet模型',
  }
]

function modify_code(){
    if(code1.value == code2.value){
        instance.post('/modify_code',{code:code1.value}).then(res=>{
            if(res){
                alert("密码修改成功")
            }else{
                alert("密码修改失败")
            }
        })
    }else{
        alert("两次密码不一致")
    }
}

function handleClose(done) {
  dialogVisible.value = false
  // 取消删除
  // done()
}
</script>

<style scoped lang="scss">
.container{
    display:flex;
    flex-direction: column;
    padding: 20px;
    width: 82vw;
    height:92.5vh;
    background-color: aliceblue;
}
.row{
    display:flex;
    flex-direction: row;
    align-items: center;
    margin-bottom: 10px;
}
.input{
    max-width: 240px;
}
</style>