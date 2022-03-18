<template>
  <div class="row">
    <div class="col-12">
      <card :title="title">
        
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
import { BaseTable } from "@/components";

export default {
  components: {
    BaseTable,
  },
  mounted() {
    axios.getAllReports().then((res) => {
      this.tableData = res.data;
    });
  },
  data() {
    return {
      title: "举报管理",
      tableColumns: [
        "report_id",
        "reporter",
        "report_content",
        "plog_id",
        "plog_name",
        "plog_content",
        "poster",
      ],
      tableData: [],
    };
  },
};
</script>
<style>
</style>
