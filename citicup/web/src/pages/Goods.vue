<template>
  <div class="card">
    <div class="card-header">
      <h2 class="title">商城商品管理</h2>
      <base-button type="primary" @click="showAdd()">增加商品</base-button>
      <el-dialog :visible.sync="addVisible" width="1100px" top="20px">
        <div
          style="
            width: 100%;
            height: 100%;
            background-color: white;
            padding: 100px 50px;
          "
        >
          <div class="row">
            <div class="col-md-8">
              <edit-profile-form :model="addedGood"> </edit-profile-form>
            </div>
            <div class="col-md-4">
              <user-card :good="model"></user-card>
              <base-button type="primary" @click="addGood()">添加</base-button>
              <base-button type="default" @click="cancelAdd()"
                >取消</base-button
              >
            </div>
          </div>
        </div>
      </el-dialog>
      <el-dialog :visible.sync="editVisible" width="1100px" top="20px">
        <div
          style="
            width: 100%;
            height: 100%;
            background-color: white;
            padding: 100px 50px;
          "
        >
          <div class="row">
            <div class="col-md-8">
              <edit-profile-form :model="model"> </edit-profile-form>
            </div>
            <div class="col-md-4">
              <user-card :good="model"></user-card>
              <base-button type="primary" @click="editGood()">编辑</base-button>
              <base-button type="default" @click="cancelEdit()"
                >取消</base-button
              >
            </div>
          </div>
        </div>
      </el-dialog>
    </div>
    <div class="card-body all-icons">
      <div class="uk-grid">
        <div
          class="font-icon-list col-lg-2 col-md-3 col-sm-4 col-xs-6 col-xs-6"
          v-for="item in this.myCollects"
          :key="item.id"
        >
          <div class="font-icon-detail">
            <div
              class="leftimg"
              :style="{
                backgroundImage:
                  'url(' + (item.imagePath ? item.imagePath : baseImg) + ')',
                backgroundSize: '100% 100%',
                backgroundRepeat: 'no-repeat',
              }"
            ></div>
            <p>{{ item.goodName }}</p>
            <base-button
              :id="item.id"
              type="info"
              size="sm"
              @click="showEdit(item.id)"
              >编辑</base-button
            >
            <base-button
              :id="item.id"
              type="default"
              size="sm"
              @click="removeGood(item.id)"
              >移除</base-button
            >
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "../axios";
import EditProfileForm from "./Profile/EditProfileForm";
import UserCard from "./Profile/UserCard";
export default {
  components: {
    EditProfileForm,
    UserCard,
  },
  mounted() {
    axios.getAllGoods().then((res) => {
      console.log(res.data);
      this.myCollects = res.data;
    });
  },
  data() {
    return {
      baseImg:
        "https://images.unsplash.com/photo-1607083206968-13611e3d76db?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8Y291cG9ufGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60",
      addVisible: false,
      editVisible: false,
      myCollects: [],
      addedGood: {},
      model: {},
    };
  },
  methods: {
    showAdd() {
      this.addVisible = true;
    },
    cancelAdd() {
      this.addVisible = false;
    },
    cancelEdit() {
      this.editVisible = false;
    },
    showEdit(id) {
      this.editVisible = true;
      console.log(id);
      axios.getGoodById(id).then((res) => {
        this.model = res.data[0];
      });
    },
    editGood() {
      let data = {
        id: this.model.id,
        good_name: this.model.goodName,
        good_type: parseInt(this.model.goodTypeId),
        good_description: this.model.goodDescription,
        good_carboncurrency: parseInt(this.model.goodCarbonCurrency),
        good_left: parseInt(this.model.goodLeft),
        image_path: this.model.imagePath,
      };
      axios
        .editGood(data)
        .then((res) => {
          this.editVisible = false;
          console.log(res);
          alert("修改成功");
          axios.getAllGoods().then((res) => {
            console.log(res.data);
            this.myCollects = res.data;
          });
        })
        .catch((err) => {
          console.log(data);
          console.log(err);
          alert("修改失败");
        });
    },
    addGood() {
      let data = {
        good_name: this.addedGood.goodName,
        good_type: parseInt(this.addedGood.goodTypeId),
        good_description: this.addedGood.goodDescription,
        good_carboncurrency: parseInt(this.addedGood.goodCarbonCurrency),
        good_left: parseInt(this.addedGood.goodLeft),
        image_path:
          "https://images.unsplash.com/photo-1607083206968-13611e3d76db?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8Y291cG9ufGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60",
      };
      axios
        .addGood(data)
        .then((res) => {
          console.log(res);
          alert("添加成功");
          this.addVisible = false;
          axios.getAllGoods().then((res) => {
            console.log(res.data);
            this.myCollects = res.data;
          });
        })
        .catch((err) => {
          console.log(data);
          console.log(err);
          alert("添加失败");
        });
    },
    removeGood(id) {
      axios
        .removeGood(id)
        .then((res) => {
          console.log(res);
          alert("移除成功");
          axios.getAllGoods().then((res) => {
            console.log(res.data);
            this.myCollects = res.data;
          });
        })
        .catch((err) => {
          console.log(err);
          alert("移除失败");
        });
    },
    notifyVue() {
      this.$notify({
        component: NotificationTemplate,
        icon: "tim-icons icon-bell-55",
        horizontalAlign: "top",
        verticalAlign: "right",
        type: "success",
        timeout: 0,
      });
    },
  },
};
</script>
<style lang="scss" scoped>
.leftimg {
  width: 170px;
  height: 129px;
}
</style>
