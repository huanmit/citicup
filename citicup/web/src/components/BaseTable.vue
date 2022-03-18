<template>
  <table class="table tablesorter" :class="tableClass">
    <el-dialog :visible.sync="refuseVisible" width="1000px" top="20px">
      <div
        style="
          width: 100%;
          height: 100%;
          background-color: white;
          padding: 50px 50px;
        "
      >
        <card>
          <div class="row">
            <div class="col-md-12">
              <div class="row">
                <div class="col-md-8" style="color: black">
                  <base-input>
                    <label>拒绝理由</label>
                    <textarea
                      rows="8"
                      cols="80"
                      class="form-control"
                      placeholder="在这里输入拒绝理由"
                      v-model="reason"
                    >
                    </textarea>
                  </base-input>
                </div>
              </div>
            </div>
            <div class="col-md-12" style="text-align: center">
              <base-button type="primary" @click="refuse()">确认</base-button>
              <base-button type="default" @click="refuseCancel()"
                >取消</base-button
              >
            </div>
          </div></card
        >
      </div>
    </el-dialog>
    <thead :class="theadClasses">
      <tr>
        <th>id</th>
        <th>举报者</th>
        <th>举报内容</th>
        <th>贴子id</th>
        <th>标题</th>
        <th>帖子内容</th>
        <th>发布者</th>
        <th>通过</th>
        <th>拒绝</th>
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
          <base-button type="success" @click="pass(item.report_id)"
            >通过</base-button
          >
        </td>
        <td>
          <base-button type="danger" @click="showRefuse(item.report_id)"
            >拒绝</base-button
          >
        </td>
      </tr>
    </tbody>
  </table>
</template>


<script>
import axios from "@/axios";
export default {
  name: "base-table",
  data() {
    return {
      refuseVisible: false,
      reportId: 1,
      refuseInfo: {},
      reason: "",
    };
  },
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
    showRefuse(id) {
      this.refuseVisible = true;
      this.reportId = id;
    },
    refuse() {
      let uid = this.$store.state.user.id;
      let data = {
        report_id: this.reportId,
        admin_user: uid,
        result: 0,
        result_detail: this.reason,
      };
      axios
        .Report(data)
        .then((res) => {
          this.refuseVisible = false;
          console.log(res);
          alert("拒绝成功");
          location.reload();
        })
        .catch((err) => {
          console.log(err);
        });
    },
    pass(id) {
      let uid = this.$store.state.user.id;
      let data = {
        report_id: id,
        admin_user: uid,
        result: 1,
        result_detail: "通过还需要理由吗？",
      };
      console.log(data);
      axios
        .Report(data)
        .then((res) => {
          console.log(res);
          alert("审核通过");
          location.reload();
        })
        .catch((err) => {
          console.log(err);
        });
    },
    refuseCancel() {
      this.refuseVisible = false;
    },
  },
};
</script>
<style>
</style>
