<template>
  <div class="row">
    <div class="col-12">
      <h2 class="title">帖子类型管理</h2>
      <card>
        <base-button type="primary" @click="showAdd()"
          >增加帖子类型</base-button
        >
        <el-dialog :visible.sync="addVisible" width="1000px" top="20px">
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
                <base-button type="primary" @click="addPlogType()"
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
import BaseTable from "@/components/BaseTable_1";
import EditProfileForm from "@/pages/PlogType/EditProfileForm";
export default {
  components: {
    BaseTable,
    EditProfileForm,
  },
  mounted() {
    axios.getAllPlogTypes().then((res) => {
      console.log(res.data);
      let raw = res.data;
      let total = [];
      raw.forEach((item) => {
        let data = {
          id: item.id,
          typename: item.typeName,
          typecarboncurrency: item.typeCarbonCurrency,
        };
        total.push(data);
      });
      this.tableData = total;
      console.log(this.tableData);
    });
  },
  data() {
    return {
      addedType: {},
      title: "低碳行为类型",
      addVisible: false,
      tableData: [],
      tableColumns: ["id", "typeName", "typeCarbonCurrency"],
    };
  },
  methods: {
    showAdd() {
      this.addVisible = true;
    },
    cancelAdd() {
      this.addVisible = false;
    },
    addPlogType() {
      let data = {
        type_name: this.addedType.typeName,
        type_coin: parseInt(this.addedType.typeCarbonCurrency),
      };
      axios
        .addPlogType(data)
        .then((res) => {
          console.log(res);
          if (res.data.error_tip) {
            alert("添加失败\n帖子类型对应的汇率应该是数字");
          } else {
            alert("添加成功");
            this.addVisible = false;
            axios.getAllPlogTypes().then((res) => {
              console.log(res.data);
              let raw = res.data;
              let total = [];
              raw.forEach((item) => {
                let data = {
                  id: item.id,
                  typename: item.typeName,
                  typecarboncurrency: item.typeCarbonCurrency,
                };
                total.push(data);
              });
              this.tableData = total;
              console.log(this.tableData);
            });
          }
        })
        .catch((err) => {
          console.log(err);
          alert("添加失败\n服务器错误");
        });
    },
  },
};
</script>
<style>
</style>
