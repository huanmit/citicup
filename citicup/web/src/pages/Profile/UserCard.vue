<template>
  <card type="user">
    <p class="card-text"></p>
    <div class="author">
      <div class="block block-one"></div>
      <div class="block block-two"></div>
      <div class="block block-three"></div>
      <div class="block block-four"></div>
      <a href="#">
        <img class="img" :src="good.imagePath" alt="baseImg" />
        <h5 class="title">{{ good.goodName }}</h5>
      </a>
      <p></p>
      <p class="description">
        {{ good.title }}
      </p>
    </div>
    <p></p>
    <p class="card-description">
      {{ good.goodDescription }}
    </p>
  </card>
</template>
<script>
export default {
  props: {
    good: {
      type: Object,
      default: () => {
        return {};
      },
    },
  },
  data: {
    baseImg:
      "https://images.unsplash.com/photo-1607083206968-13611e3d76db?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8Y291cG9ufGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60",
  },
};
</script>
<style scoped>
.leftimg {
  width: 253px;
  height: 169px;
}
</style>
