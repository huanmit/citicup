<template>
  <card>
    <h5 slot="header" class="title">增加商品信息</h5>
    <div class="row">
      <div class="col-md-5 pr-md-1">
        <base-input
          label="商品id (不可修改)"
          placeholder="id无需填写"
          v-model="model.id"
          disabled
        >
        </base-input>
      </div>
      <div class="col-md-3 px-md-1">
        <base-input
          label="商品名称"
          placeholder="请输入商品名称"
          v-model="model.goodName"
        >
        </base-input>
      </div>
      <div class="col-md-4 pl-md-1">
        <base-input
          label="商品类型"
          v-model="model.goodTypeId"
          placeholder="请输入商品类型"
        >
        </base-input>
      </div>
    </div>
    <div class="row">
      <div class="col-md-6 pr-md-1">
        <base-input
          label="兑换碳币"
          v-model="model.goodCarbonCurrency"
          placeholder="请输入兑换商品所需碳币"
        >
        </base-input>
      </div>
      <div class="col-md-6 pl-md-1">
        <base-input
          label="余量"
          v-model="model.goodLeft"
          placeholder="请输入商品余量"
        >
        </base-input>
      </div>
    </div>
    <div class="row">
      <div class="col-md-8">
        <base-input>
          <label>商品描述</label>
          <textarea
            rows="4"
            cols="80"
            class="form-control"
            placeholder="在这里输入商品描述"
            v-model="model.goodDescription"
          >
          </textarea>
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
