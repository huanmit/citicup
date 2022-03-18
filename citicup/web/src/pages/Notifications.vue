<template>
  <div class="row">
    <div class="col-md-6">
      <card>
        <h4 slot="header">商品类型管理</h4>
        <base-alert type="info">
          <div class="uk-grid">
            <div class="uk-width-1-3@m"><b>1</b></div>
            <div class="uk-width-1-3@m"><b>plain notification</b></div>
            <div class="uk-width-1-3@m">
              <base-button
                style="color: white; background-color: black"
                size="sm"
                @click="showEdit()"
                >编辑</base-button
              >
              &nbsp;&nbsp;&nbsp;
              <base-button
                style="color: white; background-color: black"
                size="sm"
                @click="checkFailed()"
                >移除</base-button
              >
            </div>
          </div>
        </base-alert>
        <base-alert type="success">
          <div class="uk-grid">
            <div class="uk-width-1-3@m"><b>1</b></div>
            <div class="uk-width-1-3@m"><b>plain notification</b></div>
            <div class="uk-width-1-3@m">
              <base-button
                style="color: white; background-color: black"
                size="sm"
                @click="showEdit()"
                >编辑</base-button
              >
              <base-button
                style="color: white; background-color: black"
                size="sm"
                @click="checkFailed()"
                >移除</base-button
              >
            </div>
          </div>
        </base-alert>
        <base-alert type="warning">
          <div class="uk-grid">
            <div class="uk-width-1-3@m"><b>1</b></div>
            <div class="uk-width-1-3@m"><b>plain notification</b></div>
            <div class="uk-width-1-3@m">
              <base-button type="primary" size="sm" @click="showEdit()"
                >编辑</base-button
              >
              <base-button type="primary" size="sm" @click="checkFailed()"
                >移除</base-button
              >
            </div>
          </div>
        </base-alert>
        <base-alert type="danger">
          <div class="uk-grid">
            <div class="uk-width-1-3@m"><b>1</b></div>
            <div class="uk-width-1-3@m"><b>plain notification</b></div>
            <div class="uk-width-1-3@m">
              <base-button type="primary" size="sm" @click="showEdit()"
                >编辑</base-button
              >
              <base-button type="primary" size="sm" @click="checkFailed()"
                >移除</base-button
              >
            </div>
          </div>
        </base-alert>
      </card>
    </div>
    <div class="col-md-6">
      <card>
        <h4 slot="header">Notifications states</h4>
        <base-alert type="primary" dismissible>
          <span
            ><b> Primary - </b> This is a regular notification made with
            ".alert-primary"</span
          >
        </base-alert>
        <base-alert type="primary" dismissible>
          <span
            ><b> Info - </b> This is a regular notification made with
            ".alert-info"</span
          >
        </base-alert>
        <base-alert type="primary" dismissible>
          <span
            ><b> Success - </b> This is a regular notification made with
            ".alert-success"</span
          >
        </base-alert>
        <base-alert type="warning" dismissible>
          <span
            ><b> Warning - </b> This is a regular notification made with
            ".alert-warning"</span
          >
        </base-alert>
        <base-alert type="danger" dismissible>
          <span
            ><b> Danger - </b> This is a regular notification made with
            ".alert-danger"</span
          >
        </base-alert>
      </card>
    </div>
    <div class="col-md-12">
      <card>
        <div class="places-buttons">
          <div class="row">
            <div class="col-md-6 ml-auto mr-auto text-center">
              <h4 class="card-title">
                Notifications Places
                <p class="category">Click to view notifications</p>
              </h4>
            </div>
          </div>
          <div class="row">
            <div class="col-lg-8 ml-auto mr-auto">
              <div class="row">
                <div class="col-md-4">
                  <base-button
                    type="primary"
                    block
                    @click="notifyVue('top', 'left')"
                    >Top Left</base-button
                  >
                </div>
                <div class="col-md-4">
                  <base-button
                    type="primary"
                    block
                    @click="notifyVue('top', 'center')"
                    >Top Center</base-button
                  >
                </div>
                <div class="col-md-4">
                  <base-button
                    type="primary"
                    block
                    @click="notifyVue('top', 'right')"
                    >Top Right</base-button
                  >
                </div>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-lg-8 ml-auto mr-auto">
              <div class="row">
                <div class="col-md-4">
                  <base-button
                    type="primary"
                    block
                    @click="notifyVue('bottom', 'left')"
                    >Bottom Left</base-button
                  >
                </div>
                <div class="col-md-4">
                  <base-button
                    type="primary"
                    block
                    @click="notifyVue('bottom', 'center')"
                    >Bottom Center</base-button
                  >
                </div>
                <div class="col-md-4">
                  <base-button
                    type="primary"
                    block
                    @click="notifyVue('bottom', 'right')"
                    >Bottom Right</base-button
                  >
                </div>
              </div>
            </div>
          </div>
        </div>
      </card>
    </div>
  </div>
</template>
<script>
import NotificationTemplate from "./Notifications/NotificationTemplate";
import { BaseAlert } from "@/components";

export default {
  components: {
    BaseAlert,
  },
  data() {
    return {
      type: ["", "info", "success", "warning", "danger"],
      notifications: {
        topCenter: false,
      },
    };
  },
  methods: {
    notifyVue(verticalAlign, horizontalAlign) {
      const color = Math.floor(Math.random() * 4 + 1);
      this.$notify({
        component: NotificationTemplate,
        icon: "tim-icons icon-bell-55",
        horizontalAlign: horizontalAlign,
        verticalAlign: verticalAlign,
        type: this.type[color],
        timeout: 0,
      });
    },
  },
};
</script>
<style>
</style>
