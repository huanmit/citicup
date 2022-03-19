<template>
  <div class="login">
    <div class="login-box wow fadeInLeft">
      <div class="left">
        <div class="head-bar">
          <div class="icon" @click="goBack()"></div>
        </div>
        <div class="main">
          <div class="main-title">登录</div>
          <div class="main-form">
            <input
              :class="{
                'login-input': true,
                'login-input-err': this.userNameErr,
              }"
              placeholder="用户名"
              @focus="resetErr"
              v-model="id"
            />
            <div class="input-check" v-show="userNameErr">
              {{ this.userNameInfo }}
            </div>
            <input
              :class="{ 'login-input': true, 'login-input-err': this.pswErr }"
              placeholder="密码"
              type="password"
              @focus="resetErr"
              v-model="password"
            />
            <div class="input-check" v-show="pswErr">{{ this.pswInfo }}</div>
          </div>
          <div class="main-lower">
            <div class="login-btn" @click="login()">登录</div>
            <div class="register" @click="goRegister()">注册</div>
          </div>
        </div>
        <div class="bottom">
          <div class="bottom-text"></div>
        </div>
      </div>
      <div class="right">
        <div class="title">Choose a low-carbon life</div>
        <div class="content">
          Be a builder of ecological civilization<br />attain a substantial
          carbon coin asset
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { WOW } from "wowjs";
import axios from "../axios";
export default {
  mounted() {
    this.$nextTick(() => {
      // 在dom渲染完后,再执行动画
      const wow = new WOW({
        live: false,
      });
      wow.init();
    });
  },
  data() {
    return {
      userNameInfo: "", //用户名错误提示
      pswInfo: "", //密码错误提示
      id: "",
      password: "",
      role: "",
    };
  },
  computed: {
    userNameErr: function () {
      return this.userNameInfo != "";
    },
    pswErr: function () {
      return this.pswInfo != "";
    },
  },
  methods: {
    goBack() {
      this.$router.push("/");
    },
    goRegister() {
      this.$router.push("/register");
    },
    login() {
      if (this.userName == "") {
        this.userNameInfo = "用户名不能为空";
        return;
      }
      if (this.password == "") {
        this.pswInfo = "请输入密码";
        return;
      }

      let data = {
        id: this.id,
        password: this.password,
      };

      console.log(data);

      axios
        .userLogin(data)
        .then((res) => {
          console.log(res.data);
          if (res.data.ifSuccess == false) {
            this.pswInfo = "用户名或密码错误";
          } else {
            // let token=res.data.data.token;
            // let data=token;
            // axios.getUserByToken(data)
            // .then(res=>{
            //   console.log(res.data.role);
            //   let user=res.data;
            //   this.$store.commit('LOGIN',token);//mutation LOGIN
            //   this.$store.commit('USER',user);
            //   this.$store.commit('LOGIN');//mutation LOGIN
            //     let redirect = decodeURIComponent(this.$route.query.redirect || '/');
            //     this.$router.push(redirect);
            // })
            let token = res.data.token;
            this.$store.commit("LOGIN", token); //mutation LOGIN
            this.$store.commit("USER", data);
            this.$store.commit("LOGIN"); //mutation LOGIN
            this.$router.push("/home/goods");
          }
        })
        .catch((err) => {
          this.pswInfo = "用户名或密码错误";
          console.log(err);
        });
    },

    resetErr() {
      this.userNameInfo = "";
      this.pswInfo = "";
    },
  },
};
</script>

<style lang="scss" scoped>
.login {
  position: absolute;
  background-color: whitesmoke;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  //overflow-x: hidden;
  .login-box {
    height: 800px;
    width: 1000px;
    border-radius: 15px;
    background-color: gray;
    display: flex;
    flex-direction: row;
    .left {
      height: 100%;
      width: 50%;
      border-top-left-radius: 15px;
      border-bottom-left-radius: 15px;
      background-color: white;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      align-items: center;
      .head-bar {
        width: 100%;
        height: 35px;
        padding-top: 10px;
        padding-left: 10px;
        .icon {
          height: 25px;
          width: 25px;
          background-image: url("../assets/back.png");
          background-size: cover;
          background-position: center;
          background-repeat: no-repeat;
          transition: all 0.3s ease;

          &:hover {
            transform: scale(1.2);
          }
        }
      }

      .main {
        width: 100%;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: center;
        padding-left: 12%;
        padding-right: 12%;
        margin-bottom: 50px;
        transition: all 0.3s ease;
        .nav-bar {
          display: flex;
          flex-direction: row;
          justify-content: center;
          align-items: center;
          .split {
            margin-left: 15px;
            margin-right: 18px;
            color: gray;
          }
          .nav-item {
            user-select: none;
            font-size: 15.6px;
            color: #222222;
            transition: all 0.3s ease;
            text-decoration: none;
            &:hover {
              color: #e63a28;
            }
          }
        }
        .main-title {
          font-size: 34px;
          color: rgb(49, 49, 49);
          //margin-bottom: 20px;
        }
        .main-form {
          display: flex;
          flex-direction: column;
          align-items: center;
          width: 100%;
          .login-input {
            width: 100%;
            height: 44px;
            border-radius: 22px;
            outline: none;
            border: 1px solid #e5e5e5;
            margin-top: 20px;
            transition: 0.2s ease-in-out;
            font-size: 15px;
            color: #222222;
            padding-left: 20px;
            padding-right: 10px;
            transition: all 0.3s ease;
            &:focus {
              border: #2f80eb 1px solid;
            }
          }

          .login-input-err {
            border: #eb3c2f 1px solid;
          }

          .input-check {
            user-select: none;
            width: 100%;
            padding-left: 20px;
            margin-top: 3px;
            font-size: 0.3rem;
            color: rgb(248, 52, 52);
          }
        }

        .main-lower {
          //padding-left: 10px;
          padding-right: 10px;
          margin-top: 20px;
          width: 100%;
          display: flex;
          flex-direction: row;
          justify-content: flex-start;
          align-items: center;
          .register {
            user-select: none;
            font-size: 13px;
            color: gray;
            transition: all 0.3s ease;

            &:hover {
              color: #276ac2;
            }
          }
          .login-btn {
            user-select: none;
            width: 80px;
            height: 36px;
            border-radius: 18px;
            font-size: 15.6px;
            background-color: #2f80eb;
            color: white;
            display: flex;
            flex-direction: row;
            justify-content: center;
            align-items: center;
            margin-right: 20px;
            transition: all 0.3s ease;

            &:hover {
              background-color: #276ac2;
            }
          }
        }
      }

      .bottom {
        width: 100%;
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        padding-left: 12%;
        padding-right: 12%;
        padding-bottom: 15px;
        .bottom-text {
          user-select: none;
          font-size: 13px;
          color: gray;
          transition: all 0.3s ease;

          &:hover {
            color: #276ac2;
          }
        }
      }
    }
    .right {
      height: 100%;
      width: 65%;
      border-top-right-radius: 15px;
      border-bottom-right-radius: 15px;
      background-color: lightblue;
      background-image: url("../assets/bg-banner-custome.jpg");
      background-size: cover;
      background-position: 80% 50%;
      background-repeat: no-repeat;
      padding: 30px;
      padding-left: 40px;
      .title {
        font-size: 30px;
        margin-top: 55%;
      }
      .content {
        margin-top: 5px;
        color: gray;
        font-size: 15.6px;
        width: 300px;
      }
    }
  }
}
</style>
