<script setup lang="ts">
import {ref, reactive} from "vue";
import instance from "@/service";
import {useRouter} from "vue-router";
const dialogFormVisible = ref(true)
const verify_code_visible = ref(false)
const formLabelWidth = ref("140px")
const route = useRouter()
const form = reactive({
  email: '',
  verify: '',
  password1: '',
  password2: '',
  delivery: false,
  type: [],
  resource: '',
  desc: '',
})
function Login(){
  console.log(form)
  const formData = new FormData()
  formData.append("email", form.email)
  formData.append("password", form.password1)
  instance.post("/login", formData).then(res => {
    if(res){
      dialogFormVisible.value = false
      //localStorage.setItem("token", res.data.token)
      localStorage.setItem("email", form.email)
      route.push("./load")
      console.log("登录成功")
    }else{
      console.log("登录失败,账号或者密码错误")
    }
  })
}
function register(){
  console.log(form)
  if(form.password1 != form.password2){
    alert("两次密码不一致")
    return
  }
  if(form.verify == ""){
    alert("验证码不能为空")
    return
  }
  if(form.email == ""){
    alert("邮箱不能为空")
    return
  }
  if(form.password1 == ""){
    alert("密码不能为空")
    return
  }
  if(form.password2 == ""){
    alert("确认密码不能为空")
    return
  }
  const formData = new FormData()
  formData.append("email", form.email)
  formData.append("password", form.password1)
  formData.append("verify", form.verify)
  instance.post("/register", formData).then(res => {
    if(String(res)=="ok"){
      console.log("注册成功")
      dialogFormVisible.value = false
      localStorage.setItem("email", form.email)
      route.push("./load")
    }else{
      alert("注册失败,邮箱重复或其他问题")
      console.log("邮箱重复或其他问题")
    }
  })
}
function send_verify_code(){
  const formData = new FormData()
  formData.append("email", form.email)
  instance.post("/send_verify_code", formData).then(res => {
    if(res){
      console.log("验证码发送成功")
    }else{
      console.log("验证码发送失败")
    }
  })
}
</script>

<template>

  <div>
    <el-dialog :closeOnClickModal="false" :closeOnPressEscape="false" :showClose="false"  v-model="dialogFormVisible" title="用户登录" width="500">
      <el-form :model="form" class="form">
        <el-form-item label="用户邮箱" :label-width="formLabelWidth">
          <el-input v-model="form.email" autocomplete="off" />
        </el-form-item>
        <el-form-item label="密码" :label-width="formLabelWidth">
          <el-input v-model="form.password1" />
        </el-form-item>
        <el-form-item v-if="verify_code_visible" label="确认密码" :label-width="formLabelWidth">
          <el-input v-model="form.password2" />
        </el-form-item>
        <el-form-item v-if="verify_code_visible" label="验证码" :label-width="formLabelWidth" >
          <div class="verify_code">
            <el-input v-model="form.verify" />
            <el-button type="primary" @click="send_verify_code">获取验证码</el-button>
          </div>
        </el-form-item>
      </el-form>
      <br>
      <template #footer>
        <div class="dialog-footer">
          <el-button v-if="!verify_code_visible" @click="verify_code_visible = true">注册</el-button>
          <el-button v-if="verify_code_visible" @click="register">注册</el-button>
          <el-button v-if="!verify_code_visible" type="primary" @click="Login">
            登录
          </el-button>
          <el-button v-if="verify_code_visible" type="primary" @click="verify_code_visible = false">
            取消
          </el-button>
        </div>
      </template>
    </el-dialog>
  </div>

</template>

<style scoped>
.verify_code{
  display: flex;
  width: 100%;
}
.form{
  text-align: right;
}
</style>