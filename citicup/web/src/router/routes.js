import DashboardLayout from "@/layout/dashboard/DashboardLayout.vue";
// GeneralViews
import NotFound from "@/pages/NotFoundPage.vue";

// Admin pages
// const Dashboard = () => import(/* webpackChunkName: "dashboard" */"@/pages/Dashboard.vue");
const GoodType = () => import(/* webpackChunkName: "common" */ "@/pages/GoodType.vue");
const Goods = () => import(/* webpackChunkName: "common" */ "@/pages/Goods.vue");
const Typography = () => import(/* webpackChunkName: "common" */ "@/pages/Report.vue");
const PlogType = () => import(/* webpackChunkName: "common" */ "@/pages/PlogType.vue");
const Register = () => import(/* webpackChunkName: "common" */ "@/pages/Register.vue");
const Login = () => import(/* webpackChunkName: "common" */ "@/pages/Login.vue");

const routes = [
  {
    path: "/",
    component: Login,
    redirect: "/login",
  },
  {
    path: "/login",
    name: "login",
    component: Login
  },
  {
    path: "/register",
    name: "register",
    component: Register
  },
  {
    path: "/home",
    component: DashboardLayout,
    redirect: "/goods",
    children: [
      {
        path: "goodType",
        name: "goodType",
        component: GoodType
      },
      {
        path: "goods",
        name: "goods",
        component: Goods
      },
      {
        path: "report",
        name: "report",
        component: Typography
      },
      {
        path: "plogType",
        name: "plogType",
        component: PlogType
      },
    ]
  },

  { path: "*", component: NotFound },
];

/**
 * Asynchronously load view (Webpack Lazy loading compatible)
 * The specified component must be inside the Views folder
 * @param  {string} name  the filename (basename) of the view to load.
function view(name) {
   var res= require('../components/Dashboard/Views/' + name + '.vue');
   return res;
};**/

export default routes;
