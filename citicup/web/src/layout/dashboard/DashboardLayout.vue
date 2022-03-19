<template>
  <div class="wrapper">
    <side-bar data-background-color="white">
      <template slot="links">
        <sidebar-link
          to="/home/goods"
          :name="$t('sidebar.icons')"
          icon="tim-icons icon-cart"
        />
        <sidebar-link
          to="/home/goodType"
          :name="$t('sidebar.userProfile')"
          icon="tim-icons icon-tag"
        />
        <sidebar-link
          to="/home/plogType"
          :name="$t('sidebar.tableList')"
          icon="tim-icons icon-tag"
        />
        <sidebar-link
          to="/home/report"
          :name="$t('sidebar.typography')"
          icon="tim-icons icon-alert-circle-exc"
        />
      </template>
    </side-bar>
    <div class="main-panel">
      <top-navbar></top-navbar>

      <dashboard-content @click.native="toggleSidebar"> </dashboard-content>

      <content-footer></content-footer>
    </div>
  </div>
</template>
<style lang="scss">
</style>
<script>
import TopNavbar from "./TopNavbar.vue";
import ContentFooter from "./ContentFooter.vue";
import DashboardContent from "./Content.vue";
import MobileMenu from "./MobileMenu";
export default {
  components: {
    TopNavbar,
    ContentFooter,
    DashboardContent,
    MobileMenu,
  },
  methods: {
    toggleSidebar() {
      if (this.$sidebar.showSidebar) {
        this.$sidebar.displaySidebar(false);
      }
    },
  },
};
</script>
