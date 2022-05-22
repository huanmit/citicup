<template>
  <footer class="footer">
    <div class="container-fluid">
      <div class="copyright">
        © {{ year }} made with <i class="tim-icons icon-heart-2"></i> by
        <a href="https://github.com/lori0423" target="_blank" rel="noopener"
          >Lori</a
        >&nbsp;
      </div>
    </div>
  </footer>
</template>
<script>
export default {
  data() {
    return {
      year: new Date().getFullYear(),
    };
  },
};
</script>
<style>
</style>
