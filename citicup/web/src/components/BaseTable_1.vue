<template>
  <card :title="title">
    <el-dialog :visible.sync="editVisible" width="900px" top="10px">
      <div
        style="
          width: 100%;
          height: 100%;
          background-color: white;
          padding: 40px 40px;
        "
      >
        <div class="row">
          <div class="col-md-12">
            <edit-profile-form :model="addedType"> </edit-profile-form>
          </div>
          <div class="col-md-12" style="text-align: center">
            <base-button type="primary" @click="editType()">保存</base-button>
            <base-button type="default" @click="cancelEdit()">取消</base-button>
          </div>
        </div>
      </div>
    </el-dialog>
    <table class="table tablesorter" :class="tableClass">
      <thead :class="theadClasses">
        <tr>
          <th>id</th>
          <th>类型名</th>
          <th>与碳币汇率</th>
          <th>编辑</th>
          <th>删除</th>
        </tr>
      </thead>
      <tbody :class="tbodyClasses">
        <tr v-for="(item, index) in data" :key="index">
          <slot :row="item">
            <td v-for="(column, index) in columns" :key="index">
              {{ itemValue(item, column) }}
            </td>
          </slot>
          <td>
            <base-button type="info" @click="showEdit(item.id)"
              >编辑</base-button
            >
          </td>
          <td>
            <base-button type="danger" @click="removeType(item.id)"
              >删除</base-button
            >
          </td>
        </tr>
      </tbody>
    </table>
  </card>
</template>
<script>
import axios from "@/axios";
import EditProfileForm from "../pages/PlogType/EditProfileForm";
export default {
  components: {
    EditProfileForm,
  },
  name: "base-table-1",
  props: {
    columns: {
      type: Array,
      default: () => [],
      description: "Table columns",
    },
    data: {
      type: Array,
      default: () => [],
      description: "Table data",
    },
    type: {
      type: String, // striped | hover
      default: "",
      description: "Whether table is striped or hover type",
    },
    theadClasses: {
      type: String,
      default: "",
      description: "<thead> css classes",
    },
    tbodyClasses: {
      type: String,
      default: "",
      description: "<tbody> css classes",
    },
  },
  data() {
    return { editVisible: false, addedType: {}, title: "" };
  },
  computed: {
    tableClass() {
      return this.type && `table-${this.type}`;
    },
  },
  methods: {
    hasValue(item, column) {
      return item[column.toLowerCase()] !== "undefined";
    },
    itemValue(item, column) {
      return item[column.toLowerCase()];
    },
    cancelEdit() {
      this.editVisible = false;
    },
    showEdit(id) {
      this.editVisible = true;
      axios.getPlogType(id).then((res) => {
        console.log(res.data);
        this.addedType = res.data[0];
      });
      console.log(this.addedType);
    },
    editType() {
      let data = {
        type_name: this.addedType.typeName,
        type_coin: parseInt(this.addedType.typeCarbonCurrency),
        id: parseInt(this.addedType.id),
      };
      data = JSON.stringify(data);
      axios
        .editPlogType(data)
        .then((res) => {
          console.log(res);
          alert("修改成功");
          this.editVisible = false;
          location.reload();
        })
        .catch((err) => {
          console.log(err);
          
        });
    },
    removeType(id) {
      axios
        .removePlogType(id)
        .then((res) => {
          console.log(res);
          alert("删除成功");
        location.reload();
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>
<style>
</style>
