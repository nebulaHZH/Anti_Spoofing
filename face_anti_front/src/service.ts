//封装一个axios请求，让所有请求都走这个封装的axios请求
import axios, { AxiosRequestConfig, AxiosResponse } from 'axios';

const instance = axios.create({
    baseURL: '/api',
    timeout: 100000000,
    headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization':localStorage.getItem('token')
    },
});
instance.interceptors.request.use((config) => {
    // 在发送请求之前干点什么
    return config
}, (error) => {
    // 对请求错误做些什么
    alert("网络错误！")
    return Promise.reject(error);
})

instance.interceptors.response.use((response: AxiosResponse) => {
    // 对响应数据做点什么
    return response.data;
})

export default instance;