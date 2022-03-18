<template>
  <div class="row">
    <div class="col-12">
      <card :title="title">
        <base-button type="primary" @click="showAdd()"
          >增加商品类型</base-button
        >
        <el-dialog :visible.sync="addVisible" width="1100px" top="20px">
          <div
            style="
              width: 100%;
              height: 100%;
              background-color: white;
              padding: 50px 50px;
            "
          >
            <div class="row">
              <div class="col-md-12">
                <edit-profile-form :model="addedType"> </edit-profile-form>
              </div>
              <div class="col-md-12">
                <base-button type="primary" @click="addGoodType()"
                  >添加</base-button
                >
                <base-button type="default" @click="cancelAdd()"
                  >取消</base-button
                >
              </div>
            </div>
          </div>
        </el-dialog>
        <div class="table-responsive">
          <base-table
            :data="tableData"
            :columns="tableColumns"
            thead-classes="text-primary"
          >
          </base-table>
        </div>
      </card>
    </div>
  </div>
</template>
<script>
import axios from "../axios";
import BaseTable from "@/components/BaseTable_2";
import EditProfileForm from "@/pages/PlogType/EditGoodForm";
export default {
  components: {
    BaseTable,
    EditProfileForm,
  },
  mounted() {
    axios.getAllGoodTypes().then((res) => {
      console.log(res.data);
      let raw = res.data;
      let total = [];
      raw.forEach((item) => {
        let data = {
          id: item.id,
          goodtypename: item.goodTypeName,
        };
        total.push(data);
      });
      this.tableData = total;
      console.log(this.tableData);
    });
  },
  data() {
    return {
      addVisible: false,
      title: "商品类型管理",
      tableData: [],
      tableColumns: ["id", "goodtypename"],
      addedType: {},
    };
  },
  methods: {
    showAdd() {
      this.addVisible = true;
    },
    cancelAdd() {
      this.addVisible = false;
    },
    addGoodType() {
      let data = {
        type_name: this.addedType.typeName,
      };
      axios
        .addGoodType(data)
        .then((res) => {
          console.log(res);
          alert("添加成功");
          
          this.addVisible = false;
          axios.getAllGoodTypes().then((res) => {
            console.log(res.data);
            let raw = res.data;
            let total = [];
            raw.forEach((item) => {
              let data = {
                id: item.id,
                goodtypename: item.goodTypeName,
              };
              total.push(data);
            });
            this.tableData = total;
            console.log(this.tableData);
          });
        })
        .catch((err) => {
          console.log(data);
          console.log(err);
          alert("添加失败");
        });
    },
  },
};
</script>
<style>
</style>
