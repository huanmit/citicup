import axios from 'axios'
import store from './store'

//创建axios实例
var instance = axios.create({
    timeout: 5000, //请求超过5秒即超时返回错误
    headers: { 'Content-Type': 'application/json;charset=UTF-8' },
});

//request拦截器
instance.interceptors.request.use(
    config => {
        //判断是否存在token，如果存在的话，则每个http header都加上token
        if (store.state.token) {
            config.headers.Authorization = `Bearer ${store.state.token}`;
        }
        return config;
    }
);

// var url = 'http://101.35.194.132:9090/';  //服务器连接
var url = 'http://localhost:8000/';  //服务器连接
export default {
    //这里export的是axios
    //所以引用的方法是: import axios from '../axios.js';
    //用户注册
    userEnable(data) {
        return instance.post(url + '/auth/enable', data);
    },
    //用户登录(只是拿到token)
    userLogin(data) {
        return instance.post(url + 'web/login/', data);
    },
    //用户注册
    userRegister(data) {
        return instance.post(url + 'web/register/', data);
    },
    getUserByToken(data) {
        return instance.post(url + 'user/getUserByToken', data);
    },

    //商品相关
    getAllGoods() {
        return instance.get(url + 'store');
    },
    getGoodById(id) {
        return instance.get(url + 'good/?id=' + id);
    },
    removeGood(id) {
        return instance.delete(url + 'web/good/?id=' + id);
    },
    editGood(data) {
        return instance.put(url + 'web/good/', data);
    },
    addGood(data) {
        return instance.post(url + 'web/good/', data);
    },

    //商品类型相关
    getAllGoodTypes() {
        return instance.get(url + 'good_type');
    },
    getGoodType(id) {
        return instance.get(url + "web/good_type/?id=" + id);
    },
    editGoodType(data) {
        return instance.put(url + "web/good_type/", data);
    },
    removeGoodType(id) {
        return instance.delete(url + "web/good_type/?id=" + id);
    },
    addGoodType(data) {
        return instance.post(url + "web/good_type/", data);
    },

    //低碳行为相关
    getAllPlogTypes() {
        return instance.get(url + 'plog_type');
    },
    getPlogType(id) {
        return instance.get(url + "web/plog_type/?id=" + id);
    },
    editPlogType(data) {
        return instance.put(url + "web/plog_type/", data);
    },
    removePlogType(id) {
        return instance.delete(url + "web/plog_type/?id=" + id);
    },
    addPlogType(data) {
        return instance.post(url + "web/plog_type/", data);
    },

    //举报相关
    getAllReports() {
        return instance.get(url + 'web/get_report');
    },
    Report(data) {
        return instance.post(url + "web/reports/", data);
    }
}
