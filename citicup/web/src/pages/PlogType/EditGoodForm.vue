<template>
  <card>
    <h5 slot="header" class="title">增加帖子类型</h5>
    <div class="row">
      <div class="col-md-5 pr-md-1">
        <base-input
          label="id (不可修改)"
          placeholder="id无需填写"
          v-model="model.id"
          disabled
        >
        </base-input>
      </div>
      <div class="col-md-3 px-md-1">
        <base-input
          label="帖子类型名称"
          placeholder="请输入帖子类型名称"
          v-model="model.typeName"
        >
        </base-input>
      </div>
    </div>
  </card>
</template>
<script>
export default {
  props: {
    model: {
      type: Object,
      default: () => {
        return {};
      },
    },
  },
};
</script>
<style lang="scss" scss>
.info {
  font-size: 12px;
  color: gray;
}
</style>
